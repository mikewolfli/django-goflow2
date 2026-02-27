from ninja import NinjaAPI, Router, Schema
from ninja.errors import HttpError
from ninja_simple_jwt.auth.views.api import mobile_auth_router, web_auth_router
from ninja_simple_jwt.auth.ninja_auth import HttpJwtAuth
from typing import List

from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.contenttypes.models import ContentType
from goflow.workflow.models import Process, Activity
from goflow.runtime.models import WorkItem, ProcessInstance

api = NinjaAPI()

api.add_router("/auth/mobile/", mobile_auth_router)
api.add_router("/auth/web/", web_auth_router)

protected_router = Router(auth=HttpJwtAuth())


class ProcessOut(Schema):
    id: int
    title: str
    enabled: bool


class ActivityOut(Schema):
    id: int
    title: str
    kind: str
    process_id: int


class WorkItemOut(Schema):
    id: int
    status: str
    activity_id: int
    instance_id: int
    user_id: int | None


class WorkItemActionIn(Schema):
    condition: str | None = None


class StartProcessIn(Schema):
    process_name: str
    content_app_label: str
    content_model: str
    object_id: int
    title: str | None = None
    priority: int | None = None


def _get_allowed_process_titles():
    return getattr(settings, "GOFLOW_API_ALLOWED_PROCESS_TITLES", None)


def _get_allowed_content_types():
    return getattr(settings, "GOFLOW_API_ALLOWED_CONTENT_TYPES", None)


def _is_process_allowed(process_title: str) -> bool:
    allowed = _get_allowed_process_titles()
    if not allowed:
        return True
    return process_title in allowed


def _is_content_type_allowed(app_label: str, model: str) -> bool:
    allowed = _get_allowed_content_types()
    if not allowed:
        return True
    return f"{app_label}.{model}".lower() in {item.lower() for item in allowed}


def _require_object_ownership() -> bool:
    return getattr(settings, "GOFLOW_API_REQUIRE_OBJECT_OWNERSHIP", False)


def _get_owner_fields():
    return getattr(settings, "GOFLOW_API_OBJECT_OWNER_FIELDS", ())


def _check_object_access(user, obj) -> bool:
    owner_fields = _get_owner_fields()
    if not owner_fields:
        return not _require_object_ownership()

    def _same_user(owner_value) -> bool:
        if owner_value is None:
            return False
        owner_id = getattr(owner_value, "id", owner_value)
        user_id = getattr(user, "id", None)
        if user_id is None:
            return False
        return owner_id == user_id

    matched_owner_field = False
    for field_name in owner_fields:
        if hasattr(obj, field_name):
            matched_owner_field = True
            if _same_user(getattr(obj, field_name)):
                return True
    if matched_owner_field:
        return False
    return not _require_object_ownership()


def _serialize_workitems(workitems):
    items = []
    seen = set()
    for workitem in workitems:
        if workitem.id in seen:
            continue
        seen.add(workitem.id)
        items.append(
            {
                "id": workitem.id,
                "status": workitem.status,
                "activity_id": workitem.activity_id,
                "instance_id": workitem.instance_id,
                "user_id": workitem.user_id,
            }
        )
    return items


def _get_workitem_or_error(workitem_id: int, user):
    try:
        return WorkItem.objects.get_safe(id=workitem_id, user=user)
    except WorkItem.DoesNotExist as exc:
        raise HttpError(404, "Workitem not found") from exc
    except Exception as exc:
        raise HttpError(403, "Workitem not allowed") from exc


def _get_db_user(user):
    if not getattr(user, "is_authenticated", False):
        raise HttpError(401, "Unauthorized")
    user_model = get_user_model()
    if isinstance(user, user_model):
        return user
    user_id = getattr(user, "id", None)
    if user_id is None:
        raise HttpError(401, "Unauthorized")
    try:
        return user_model.objects.get(pk=user_id)
    except user_model.DoesNotExist as exc:
        raise HttpError(401, "Unauthorized") from exc

@protected_router.get("/me")
def me(request):
    user = getattr(request, "user", None)
    return {
        "username": getattr(user, "username", None),
        "is_authenticated": bool(getattr(user, "is_authenticated", False)),
    }


@protected_router.get("/processes", response=List[ProcessOut])
def list_processes(request):
    allowed = _get_allowed_process_titles()
    queryset = Process.objects.all()
    if allowed:
        queryset = queryset.filter(title__in=allowed)
    return queryset.values("id", "title", "enabled")


@protected_router.get("/processes/{process_id}/activities", response=List[ActivityOut])
def list_activities(request, process_id: int):
    allowed = _get_allowed_process_titles()
    if allowed and not Process.objects.filter(id=process_id, title__in=allowed).exists():
        raise HttpError(403, "Process not allowed")
    return Activity.objects.filter(process_id=process_id).values(
        "id", "title", "kind", "process_id"
    )


@protected_router.get("/workitems", response=List[WorkItemOut])
def list_workitems(request):
    db_user = _get_db_user(request.user)
    workitems = WorkItem.objects.list_safe(user=db_user)
    return _serialize_workitems(workitems)


@protected_router.get("/my/workitems", response=List[WorkItemOut])
def list_my_workitems(request):
    db_user = _get_db_user(request.user)
    workitems = WorkItem.objects.filter(user=db_user)
    return _serialize_workitems(workitems)


@protected_router.post("/workitems/{workitem_id}/activate")
def activate_workitem(request, workitem_id: int):
    db_user = _get_db_user(request.user)
    workitem = _get_workitem_or_error(workitem_id, db_user)
    workitem.activate(actor=db_user)
    return {"status": "activated", "workitem_id": workitem_id}


@protected_router.post("/workitems/{workitem_id}/complete")
def complete_workitem(request, workitem_id: int, payload: WorkItemActionIn):
    db_user = _get_db_user(request.user)
    workitem = _get_workitem_or_error(workitem_id, db_user)
    if payload.condition:
        workitem.instance.condition = payload.condition
        workitem.instance.save()
    workitem.complete(actor=db_user)
    return {"status": "completed", "workitem_id": workitem_id}


@protected_router.post("/processes/start")
def start_process(request, payload: StartProcessIn):
    db_user = _get_db_user(request.user)
    if not _is_process_allowed(payload.process_name):
        raise HttpError(403, "Process not allowed")
    if not _is_content_type_allowed(payload.content_app_label, payload.content_model):
        raise HttpError(403, "Content type not allowed")
    try:
        ctype = ContentType.objects.get(
            app_label=payload.content_app_label,
            model=payload.content_model,
        )
    except ContentType.DoesNotExist as exc:
        raise HttpError(400, "Invalid content type") from exc

    model_class = ctype.model_class()
    if not model_class:
        raise HttpError(400, "Invalid content model")

    try:
        obj = model_class.objects.get(pk=payload.object_id)
    except model_class.DoesNotExist as exc:
        raise HttpError(404, "Object not found") from exc

    if not _check_object_access(db_user, obj):
        raise HttpError(403, "Object not allowed")

    try:
        Process.objects.check_can_start(payload.process_name, db_user)
    except Exception as exc:
        raise HttpError(403, "User cannot start this process") from exc

    try:
        workitem = ProcessInstance.objects.start(
            payload.process_name,
            db_user,
            obj,
            title=payload.title,
            priority=payload.priority or 0,
        )
    except Exception as exc:
        raise HttpError(400, "Failed to start process") from exc
    return {
        "status": "started",
        "workitem_id": workitem.id,
        "instance_id": workitem.instance_id,
    }

api.add_router("/protected/", protected_router)
