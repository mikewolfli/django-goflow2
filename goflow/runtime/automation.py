#!/usr/local/bin/python
# -*- coding: utf-8 -*-
from django.conf import settings
from django.contrib.auth import get_user_model

from goflow.runtime.models import WorkItem
from goflow.runtime.sla import parse_duration
from goflow.runtime.audit import log_audit_event
from django.utils import timezone
from goflow.runtime.signals import sla_warned, sla_breached
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


def run_sla_scan():
    if not getattr(settings, 'GOFLOW_SLA_ENABLED', True):
        return {
            'sla_checked': 0,
            'sla_warned': 0,
            'sla_breached': 0,
        }

    now = timezone.now()
    sla_checked = 0
    sla_warned = 0
    sla_breached = 0
    workitems = WorkItem.objects.filter(
        status__in=('inactive', 'active'),
        activity__sla_duration__isnull=False,
    ).exclude(activity__sla_duration='')

    for workitem in workitems:
        sla_checked += 1
        try:
            breach_delta = parse_duration(workitem.activity.sla_duration)
        except Exception:
            continue

        start_at = workitem.activated_at or workitem.created_at or workitem.date
        warn_delta = None
        if workitem.activity.sla_warn:
            try:
                warn_delta = parse_duration(workitem.activity.sla_warn)
            except Exception:
                warn_delta = None

        if warn_delta and not workitem.sla_warned_at:
            if now >= (start_at + warn_delta):
                workitem.sla_warned_at = now
                workitem.save(update_fields=['sla_warned_at'])
                sla_warned += 1
                try:
                    sla_warned.send(sender=WorkItem, workitem=workitem)
                except Exception:
                    pass
                log_audit_event(
                    action='sla.warned',
                    actor=workitem.user,
                    workitem=workitem,
                    status_from=workitem.status,
                    status_to=workitem.status,
                )
                if getattr(settings, 'GOFLOW_SLA_NOTIFY', True):
                    WorkItem.objects.notify_if_needed(roles=workitem.activity.sla_roles.all())

        if not workitem.sla_breached_at and now >= (start_at + breach_delta):
            workitem.sla_breached_at = now
            workitem.last_escalation_at = now
            workitem.save(update_fields=['sla_breached_at', 'last_escalation_at'])
            sla_breached += 1
            try:
                sla_breached.send(sender=WorkItem, workitem=workitem)
            except Exception:
                pass
            log_audit_event(
                action='sla.breached',
                actor=workitem.user,
                workitem=workitem,
                status_from=workitem.status,
                status_to=workitem.status,
            )
            if getattr(settings, 'GOFLOW_SLA_NOTIFY', True):
                WorkItem.objects.notify_if_needed(roles=workitem.activity.sla_roles.all())
            if getattr(settings, 'GOFLOW_SLA_AUTO_ASSIGN', False):
                candidates = User.objects.filter(groups__in=workitem.activity.sla_roles.all()).distinct()
                if candidates.exists():
                    workitem.user = candidates.first()
                    workitem.save(update_fields=['user'])

    return {
        'sla_checked': sla_checked,
        'sla_warned': sla_warned,
        'sla_breached': sla_breached,
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
