from django.conf import settings


DEFAULT_AUDIT_ENABLED = True


def is_audit_enabled():
    return getattr(settings, 'GOFLOW_AUDIT_ENABLED', DEFAULT_AUDIT_ENABLED)


def log_audit_event(
    action,
    actor=None,
    workitem=None,
    instance=None,
    activity=None,
    transition=None,
    status_from=None,
    status_to=None,
    metadata=None,
):
    if not is_audit_enabled():
        return None

    from goflow.runtime.models import AuditEvent

    if workitem and not instance:
        instance = workitem.instance
    if workitem and not activity:
        activity = workitem.activity
    process = None
    if instance:
        process = instance.process

    event = AuditEvent.objects.create(
        action=action,
        actor=actor,
        process=process,
        instance=instance,
        workitem=workitem,
        activity=activity,
        transition=transition,
        status_from=status_from,
        status_to=status_to,
        metadata=metadata or {},
    )

    try:
        from goflow.runtime.signals import audit_event_created

        audit_event_created.send(
            sender=AuditEvent,
            event=event,
        )
    except Exception:
        pass

    if getattr(settings, 'GOFLOW_WEBHOOK_ENABLED', False):
        try:
            from goflow.runtime.webhooks import dispatch_webhooks

            dispatch_webhooks(event)
        except Exception:
            # Avoid breaking workflow execution on webhook failures.
            pass

    return event
