#!/usr/local/bin/python
# -*- coding: utf-8 -*-
try:
    from celery import shared_task
except Exception:
    def shared_task(*args, **kwargs):
        def decorator(func):
            def apply_async(call_args=None, call_kwargs=None, **options):
                return func(*(call_args or ()), **(call_kwargs or {}))

            func.delay = lambda *call_args, **call_kwargs: func(*call_args, **call_kwargs)
            func.apply_async = apply_async
            return func

        if args and callable(args[0]) and len(args) == 1 and not kwargs:
            return decorator(args[0])
        return decorator

from goflow.runtime.automation import run_timeout_scan, run_workitem_action, run_user_notification, run_sla_scan


@shared_task
def timeout_scan_task():
    return run_timeout_scan()


@shared_task
def sla_scan_task():
    return run_sla_scan()


@shared_task
def workitem_action_task(workitem_id, action='forward', kwargs=None):
    kwargs = kwargs or {}
    return run_workitem_action(workitem_id=workitem_id, action=action, **kwargs)


@shared_task
def notification_task(user_id, workitem_ids=None):
    return run_user_notification(user_id=user_id, workitem_ids=workitem_ids)
