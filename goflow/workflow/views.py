#!/usr/local/bin/python
# -*- coding: utf-8 -*-
import json

from django.shortcuts import render
from django.conf import settings
from django.contrib.auth.models import Group
from django.contrib.auth import authenticate, login, logout
from django.contrib.contenttypes.models import ContentType
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse, HttpResponseForbidden, HttpResponseBadRequest
from django.utils import timezone

from goflow.runtime.models import WorkItem
from goflow.runtime.automation import run_timeout_scan
from goflow.workflow.models import *
from goflow.workflow.safe_expressions import normalize_condition_text
from goflow.tenancy import apply_tenant_filter
from django.utils.translation import gettext_lazy as _, gettext
from django.contrib import messages


def index(request, template='workflow/index.html', extra_context={}):
    """workflow dashboard handler.
    
    template context contains following objects:
    - user
    - processes
    - roles
    
    other applications (ie runtime or apptools) should fill extra_context.
    """
    print('index request\n\n\n')
    me = request.user
    roles = Group.objects.all()
    processes = Process.objects.all()
    # optional package (ugly design)
    try:
        from goflow.apptools.models import DefaultAppModel
        obinstances = DefaultAppModel.objects.all()
    except Exception:
        obinstances = None
    
    context = {'processes':processes, 'roles':roles}
    context.update(extra_context)
    return render(request, template, context)


def debug_switch_user(request, username, password, redirect=None):
    """
    fast user switch for test purpose.
    
    parameters:
    
    username
        username
    password
        password
    redirect
        redirection url
    
    *FOR TEST ONLY*
    
    see template tag switch_users.
    """
    logout(request)
    # return HttpResponseRedirect(redirect)
    if not redirect:
        redirect = request.META['HTTP_REFERER']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            return HttpResponseRedirect(redirect)
        else:
            return HttpResponse(gettext('user is not active'))
    else:
        return HttpResponse(gettext('authentication failed'))


def userlist(request, template):
    '''
    not used
    '''
    return HttpResponse(gettext('user page.'))


def process_dot(request, id, template='goflow/process.dot'):
    """graphviz generator (**Work In Progress**).
    (**Work In Progress**)
    
    id process id
    template graphviz template
    
    context provides: process, roles, activities
    """
    process = Process.objects.get(id=int(id))
    context = {
               'process': process,
               'roles': ({'name':'role1', 'color':'red'},),
               'activities': Activity.objects.filter(process=process)
               }
    return render(request, template, context)


def cron(request=None):
    """
    (**Work In Progress**)
    TODO: move to instances ?
    """
    result = run_timeout_scan()
    
    if request:
        #request.user.message_set.create(message="cron has run.")
        messages.add_message(
            request,
            messages.INFO,
            "cron has run. transitions={timeout_transitions}, checked={checked_workitems}, triggered={triggered_workitems}".format(**result),
        )
        #if request.META.has_key('HTTP_REFERER'):
        if 'HTTP_REFERER' in request.META.keys():
            url = request.META['HTTP_REFERER']
        else:
            url = 'home/'
        return HttpResponseRedirect(url)

    return result


def workflow_designer(request, process_id):
    if not request.user.is_authenticated or not request.user.is_staff:
        return HttpResponseForbidden(gettext("Forbidden"))
    process = Process.objects.get(id=process_id)
    return render(request, "goflow/workflow_designer.html", {"process": process})


def _validate_workflow_payload(payload):
    errors = []

    def _as_bool(value):
        if isinstance(value, bool):
            return value
        if isinstance(value, str):
            return value.strip().lower() in ('1', 'true', 'yes', 'on')
        return bool(value)

    activities = payload.get('activities', [])
    transitions = payload.get('transitions', [])
    deleted_activity_ids = set(payload.get('deleted_activity_ids', []))
    deleted_transition_ids = set(payload.get('deleted_transition_ids', []))
    begin_id = payload.get('begin_id')
    end_id = payload.get('end_id')

    active_activities = [a for a in activities if a.get('client_id') not in deleted_activity_ids]
    if not active_activities:
        errors.append(gettext('At least one activity is required.'))

    valid_kinds = {value for value, _ in Activity.KIND_CHOICES}
    valid_node_types = {value for value, _ in Activity.NODE_TYPE_CHOICES}

    titles = []
    for activity in active_activities:
        title = (activity.get('title') or '').strip()
        display_title = title or gettext('Untitled')
        if not title:
            errors.append(gettext('Every activity must have a title.'))
        elif len(title) > 100:
            errors.append(gettext('Activity titles must be 100 characters or fewer.'))
        else:
            titles.append(title)

        kind = activity.get('kind') or 'standard'
        if kind not in valid_kinds:
            errors.append(gettext('Activity kind must be one of: %(choices)s.') % {
                'choices': ', '.join(sorted(valid_kinds))
            })

        node_type = activity.get('node_type') or 'standard'
        if node_type not in valid_node_types:
            errors.append(gettext('Activity node type must be one of: %(choices)s.') % {
                'choices': ', '.join(sorted(valid_node_types))
            })

        form_template = (activity.get('form_template') or '').strip()
        form_class = (activity.get('form_class') or '').strip()
        autostart = _as_bool(activity.get('autostart', False))
        autofinish = _as_bool(activity.get('autofinish', True))

        if node_type == 'gateway':
            if kind != 'dummy':
                errors.append(gettext('Activity "%(title)s": gateway nodes must use kind=dummy.') % {
                    'title': display_title
                })
            if form_template or form_class:
                errors.append(gettext('Activity "%(title)s": gateway nodes cannot bind form_template or form_class.') % {
                    'title': display_title
                })

        if node_type in ('service', 'script') and not autostart:
            errors.append(gettext('Activity "%(title)s": %(node_type)s nodes should enable autostart.') % {
                'title': display_title,
                'node_type': node_type,
            })

        if node_type == 'script' and not autofinish:
            errors.append(gettext('Activity "%(title)s": script nodes should enable autofinish.') % {
                'title': display_title
            })

        if node_type == 'notification' and form_class:
            errors.append(gettext('Activity "%(title)s": notification nodes should not use form_class.') % {
                'title': display_title
            })

    titles = [t for t in titles if t]
    if len(set(titles)) != len(titles):
        errors.append(gettext('Activity titles must be unique.'))

    activity_ids = {str(a.get('client_id')) for a in active_activities}
    if begin_id and str(begin_id) not in activity_ids:
        errors.append(gettext('Begin activity must exist in the workflow.'))
    if end_id and str(end_id) not in activity_ids:
        errors.append(gettext('End activity must exist in the workflow.'))
    if not begin_id:
        errors.append(gettext('Begin activity is required.'))
    if not end_id:
        errors.append(gettext('End activity is required.'))
    if begin_id and end_id and str(begin_id) == str(end_id):
        errors.append(gettext('Begin and End activities must be different.'))

    active_transitions = [t for t in transitions if t.get('client_id') not in deleted_transition_ids]
    if not active_transitions:
        errors.append(gettext('At least one transition is required.'))
    incoming = {str(a.get('client_id')): 0 for a in active_activities}
    outgoing = {str(a.get('client_id')): 0 for a in active_activities}
    transition_keys = set()
    outgoing_blank_conditions = {}
    for transition in active_transitions:
        input_id = str(transition.get('input_id') or '')
        output_id = str(transition.get('output_id') or '')
        condition = (transition.get('condition') or '').strip()
        name = (transition.get('name') or '').strip()
        if input_id not in activity_ids or output_id not in activity_ids:
            errors.append(gettext('Transitions must connect valid activities.'))
        if input_id and output_id and input_id == output_id:
            errors.append(gettext('Transitions cannot point to the same activity.'))
        if not condition and not name:
            errors.append(gettext('Transitions must have a name or condition.'))
        if input_id and output_id:
            key = (input_id, output_id, condition, name)
            if key in transition_keys:
                errors.append(gettext('Duplicate transitions are not allowed.'))
            transition_keys.add(key)
        if input_id and not condition:
            outgoing_blank_conditions[input_id] = outgoing_blank_conditions.get(input_id, 0) + 1
        if input_id in outgoing:
            outgoing[input_id] += 1
        if output_id in incoming:
            incoming[output_id] += 1

    # Identify isolated nodes (no incoming or outgoing transitions).
    connected = set()
    for transition in active_transitions:
        connected.add(str(transition.get('input_id')))
        connected.add(str(transition.get('output_id')))
    isolated = [a for a in active_activities if str(a.get('client_id')) not in connected]
    if isolated:
        errors.append(gettext('All activities must be connected by at least one transition.'))

    if begin_id and incoming.get(str(begin_id), 0) > 0:
        errors.append(gettext('Begin activity cannot have incoming transitions.'))
    if begin_id and outgoing.get(str(begin_id), 0) == 0:
        errors.append(gettext('Begin activity must have at least one outgoing transition.'))
    if end_id and outgoing.get(str(end_id), 0) > 0:
        errors.append(gettext('End activity cannot have outgoing transitions.'))
    if end_id and incoming.get(str(end_id), 0) == 0:
        errors.append(gettext('End activity must have at least one incoming transition.'))

    if any(count > 1 for count in outgoing_blank_conditions.values()):
        errors.append(gettext('Only one default (empty) transition is allowed per activity.'))

    # Reachability from begin.
    if begin_id:
        adjacency = {}
        for transition in active_transitions:
            adjacency.setdefault(str(transition.get('input_id')), set()).add(str(transition.get('output_id')))
        visited = set()
        stack = [str(begin_id)]
        while stack:
            current = stack.pop()
            if current in visited:
                continue
            visited.add(current)
            for nxt in adjacency.get(current, []):
                if nxt not in visited:
                    stack.append(nxt)
        unreachable = [a for a in active_activities if str(a.get('client_id')) not in visited]
        if unreachable:
            errors.append(gettext('All activities must be reachable from Begin.'))

    return errors


def workflow_graph(request, process_id):
    if not request.user.is_authenticated or not request.user.is_staff:
        return HttpResponseForbidden(gettext("Forbidden"))
    process = Process.objects.get(id=process_id)

    layout = WorkflowLayout.objects.filter(process=process).first()
    layout_map = layout.layout if layout else {}

    if request.method == "GET":
        activities = []
        for activity in Activity.objects.filter(process=process):
            position = layout_map.get(str(activity.id))
            activities.append(
                {
                    "id": activity.id,
                    "title": activity.title,
                    "kind": activity.kind,
                    "node_type": activity.node_type,
                    "autostart": activity.autostart,
                    "autofinish": activity.autofinish,
                    "form_template": activity.form_template,
                    "form_class": activity.form_class,
                    "sla_duration": activity.sla_duration,
                    "sla_warn": activity.sla_warn,
                    "position": position,
                }
            )
        transitions = Transition.objects.filter(process=process).values(
            "id",
            "name",
            "input_id",
            "output_id",
            "condition",
        )
        payload = {
            "process": {
                "id": process.id,
                "title": process.title,
                "begin_id": process.begin_id,
                "end_id": process.end_id,
            },
            "activities": list(activities),
            "transitions": list(transitions),
        }
        return JsonResponse(payload)

    if request.method != "POST":
        return HttpResponseBadRequest("Unsupported method")

    try:
        data = json.loads(request.body.decode("utf-8"))
    except Exception:
        return HttpResponseBadRequest("Invalid JSON")

    activities = data.get("activities", [])
    transitions = data.get("transitions", [])
    positions = data.get("positions", {})
    deleted_activity_ids = set(data.get("deleted_activity_ids", []))
    deleted_transition_ids = set(data.get("deleted_transition_ids", []))
    begin_id = data.get("begin_id")
    end_id = data.get("end_id")

    validation_errors = _validate_workflow_payload(data)
    if validation_errors:
        return JsonResponse({'status': 'error', 'errors': validation_errors}, status=400)

    for activity_id in deleted_activity_ids:
        Activity.objects.filter(process=process, id=activity_id).delete()
        layout_map.pop(str(activity_id), None)

    for transition_id in deleted_transition_ids:
        Transition.objects.filter(process=process, id=transition_id).delete()

    activity_map = {}
    for item in activities:
        item_id = item.get("id")
        defaults = {
            "title": item.get("title", "Activity"),
            "kind": item.get("kind", "standard"),
            "node_type": item.get("node_type", "standard"),
            "autostart": bool(item.get("autostart", False)),
            "autofinish": bool(item.get("autofinish", True)),
            "form_template": item.get("form_template") or None,
            "form_class": item.get("form_class") or None,
        }
        if item_id:
            activity = Activity.objects.get(id=item_id, process=process)
            for field, value in defaults.items():
                setattr(activity, field, value)
            activity.save()
        else:
            activity = Activity.objects.create(process=process, **defaults)
        activity_map[item.get("client_id") or activity.id] = activity.id

        position = item.get("position")
        if position:
            layout_map[str(activity.id)] = position

    for item in transitions:
        item_id = item.get("id")
        input_id = item.get("input_id")
        output_id = item.get("output_id")
        if input_id in activity_map:
            input_id = activity_map[input_id]
        if output_id in activity_map:
            output_id = activity_map[output_id]
        if not input_id or not output_id:
            continue
        defaults = {
            "name": item.get("name") or "",
            "condition": normalize_condition_text(item.get("condition") or ""),
        }
        if item_id:
            transition = Transition.objects.get(id=item_id, process=process)
            transition.input_id = input_id
            transition.output_id = output_id
            transition.name = defaults["name"]
            transition.condition = defaults["condition"]
            transition.save()
        else:
            Transition.objects.create(
                process=process,
                input_id=input_id,
                output_id=output_id,
                name=defaults["name"],
                condition=defaults["condition"],
            )

    if begin_id in activity_map:
        begin_id = activity_map[begin_id]
    if end_id in activity_map:
        end_id = activity_map[end_id]

    if begin_id:
        process.begin_id = begin_id
    if end_id:
        process.end_id = end_id
    process.save()

    return JsonResponse({'status': 'ok'})


def process_versions(request, process_id):
    if not request.user.is_authenticated or not request.user.is_staff:
        return HttpResponseForbidden("Forbidden")
    process = Process.objects.get(id=process_id)
    code = process.get_identity()
    versions = apply_tenant_filter(Process.objects.filter(code=code)).order_by('-version')
    return render(
        request,
        'goflow/process_versions.html',
        {'process': process, 'versions': versions},
    )


def process_publish(request, process_id):
    if not request.user.is_authenticated or not request.user.is_staff:
        return HttpResponseForbidden("Forbidden")
    if not request.user.has_perm('workflow.can_instantiate'):
        return HttpResponseForbidden("Permission denied")
    process = Process.objects.get(id=process_id)
    is_rollback = request.GET.get('rollback') == '1'
    if request.method == 'GET' and request.GET.get('confirm') != '1':
        return render(request, 'goflow/process_publish_confirm.html', {'process': process})
    code = process.get_identity()
    Process.objects.filter(code=code).exclude(id=process.id).update(status='retired')
    process.status = 'published'
    process.published_at = timezone.now()
    process.published_by = request.user
    if is_rollback:
        process.version_note = 'rollback to version %s' % process.version
        process.save(update_fields=['status', 'published_at', 'published_by', 'version_note'])
    else:
        process.save(update_fields=['status', 'published_at', 'published_by'])
    try:
        from goflow.runtime.audit import log_audit_event

        log_audit_event(
            action='process.published',
            actor=request.user,
            process=process,
            metadata={'rollback': is_rollback, 'version': process.version},
        )
    except Exception:
        pass
    try:
        from goflow.runtime.signals import process_published

        process_published.send(
            sender=Process,
            process=process,
            actor=request.user,
            rollback=is_rollback,
        )
    except Exception:
        pass
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


def process_clone(request, process_id):
    if not request.user.is_authenticated or not request.user.is_staff:
        return HttpResponseForbidden("Forbidden")
    if not request.user.has_perm('workflow.can_instantiate'):
        return HttpResponseForbidden("Permission denied")
    process = Process.objects.get(id=process_id)
    new_version = process.clone_as_new_version(user=request.user, note='cloned from %s' % process.version)
    return HttpResponseRedirect('../../admin/workflow/process/%d/change/' % new_version.id)


def process_diff(request, process_id):
    if not request.user.is_authenticated or not request.user.is_staff:
        return HttpResponseForbidden("Forbidden")
    compare_id = request.GET.get('compare')
    if not compare_id:
        return HttpResponseBadRequest('compare parameter required')
    base = Process.objects.get(id=process_id)
    other = Process.objects.get(id=int(compare_id))
    if base.get_identity() != other.get_identity():
        return HttpResponseBadRequest('process code mismatch')

    base_activities = {a.title for a in base.activities.all()}
    other_activities = {a.title for a in other.activities.all()}
    base_transitions = {
        (t.input.title, t.output.title, t.condition or '')
        for t in base.transitions.all()
    }
    other_transitions = {
        (t.input.title, t.output.title, t.condition or '')
        for t in other.transitions.all()
    }

    payload = {
        'base_id': base.id,
        'compare_id': other.id,
        'activities_added': sorted(list(other_activities - base_activities)),
        'activities_removed': sorted(list(base_activities - other_activities)),
        'transitions_added': sorted(list(other_transitions - base_transitions)),
        'transitions_removed': sorted(list(base_transitions - other_transitions)),
    }
    if request.GET.get('format') == 'html':
        return render(request, 'goflow/process_diff.html', payload)
    return JsonResponse(payload)

    if positions:
        for key, value in positions.items():
            layout_map[str(key)] = value

    if layout:
        layout.layout = layout_map
        layout.save()
    else:
        WorkflowLayout.objects.create(process=process, layout=layout_map)

    return JsonResponse({"status": "ok"})

