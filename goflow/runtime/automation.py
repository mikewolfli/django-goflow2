#!/usr/local/bin/python
# -*- coding: utf-8 -*-
from django.conf import settings
from django.contrib.auth import get_user_model

from goflow.runtime.models import WorkItem
from goflow.workflow.models import Transition
from goflow.workflow.safe_expressions import is_timeout_condition


User = get_user_model()


def run_timeout_scan():
    transitions = Transition.objects.all()
    timeout_transitions = [transition for transition in transitions if is_timeout_condition(transition.condition)]

    checked_workitems = 0
    triggered_workitems = 0
    for transition in timeout_transitions:
        workitems = WorkItem.objects.filter(activity=transition.input).exclude(status='complete')
        for workitem in workitems:
            checked_workitems += 1
            workitem.forward(timeout_forwarding=True)
            triggered_workitems += 1

    return {
        'timeout_transitions': len(timeout_transitions),
        'checked_workitems': checked_workitems,
        'triggered_workitems': triggered_workitems,
    }


def run_workitem_action(workitem_id, action='forward', actor_username=None):
    workitem = WorkItem.objects.get(id=int(workitem_id))
    actor_name = actor_username or getattr(settings, 'WF_USER_AUTO', None)
    actor = None
    if actor_name:
        actor = User.objects.get(username=actor_name)

    if action == 'activate':
        if not actor:
            raise ValueError('actor is required for activate action')
        workitem.activate(actor=actor)
        return {'status': 'activated', 'workitem_id': workitem.id}

    if action == 'complete':
        if not actor:
            raise ValueError('actor is required for complete action')
        workitem.complete(actor=actor)
        return {'status': 'completed', 'workitem_id': workitem.id}

    if action == 'forward':
        workitem.forward(timeout_forwarding=True)
        return {'status': 'forwarded', 'workitem_id': workitem.id}

    raise ValueError('unsupported action: %s' % action)


def run_user_notification(user_id, workitem_ids=None):
    user = User.objects.get(id=int(user_id))
    if workitem_ids:
        workitems = WorkItem.objects.filter(id__in=workitem_ids)
        if workitems.exists():
            WorkItem.objects.notify_if_needed(user=user)
            return {'status': 'notified', 'user_id': user.id, 'workitems': list(workitems.values_list('id', flat=True))}
    WorkItem.objects.notify_if_needed(user=user)
    return {'status': 'notified', 'user_id': user.id}
