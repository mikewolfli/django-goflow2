from django.conf import settings


def compensate_refund(workitem, reason=None):
    # Example compensation handler to mark a refund request in the workflow object.
    wf_object = workitem.instance.wfobject()
    if hasattr(wf_object, 'refund_status'):
        wf_object.refund_status = 'compensated'
        if hasattr(wf_object, 'save'):
            wf_object.save()
    return {
        'handled': True,
        'reason': reason or '',
        'workitem_id': workitem.id,
    }


def compensate_notify(workitem, reason=None):
    # Example handler that only emits a log-style marker on the workflow object.
    wf_object = workitem.instance.wfobject()
    message = 'compensation triggered'
    if reason:
        message = '%s: %s' % (message, reason)
    if hasattr(wf_object, 'history'):
        wf_object.history += '\n>>> %s' % message
        if hasattr(wf_object, 'save'):
            wf_object.save()
    if hasattr(settings, 'LOGGING_FILE'):
        try:
            from goflow.workflow.logger import log

            log.info('compensation_notify workitem=%s reason=%s', workitem.id, reason)
        except Exception:
            pass
    return {
        'handled': True,
        'reason': reason or '',
        'workitem_id': workitem.id,
    }
