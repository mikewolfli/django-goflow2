#!/usr/local/bin/python
# -*- coding: utf-8 -*-
from django.conf import settings
from django.utils.module_loading import import_string


class BaseSchedulerBackend(object):
    def schedule_timeout_scan(self):
        raise NotImplementedError

    def schedule_workitem_action(self, workitem_id, action='forward', **kwargs):
        raise NotImplementedError

    def schedule_notification(self, user_id, workitem_ids=None):
        raise NotImplementedError


class CronSchedulerBackend(BaseSchedulerBackend):
    def schedule_timeout_scan(self):
        return {
            'scheduled': False,
            'backend': 'cron',
            'message': 'Use goflow_cron management command via linux cron',
        }

    def schedule_workitem_action(self, workitem_id, action='forward', **kwargs):
        from goflow.runtime.automation import run_workitem_action

        run_workitem_action(workitem_id=workitem_id, action=action, **kwargs)
        return {'scheduled': True, 'backend': 'cron', 'inline': True}

    def schedule_notification(self, user_id, workitem_ids=None):
        from goflow.runtime.automation import run_user_notification

        run_user_notification(user_id=user_id, workitem_ids=workitem_ids)
        return {'scheduled': True, 'backend': 'cron', 'inline': True}


class CelerySchedulerBackend(BaseSchedulerBackend):
    def schedule_timeout_scan(self):
        from goflow.runtime import tasks

        tasks.timeout_scan_task.delay()
        return {'scheduled': True, 'backend': 'celery'}

    def schedule_workitem_action(self, workitem_id, action='forward', **kwargs):
        from goflow.runtime import tasks

        tasks.workitem_action_task.delay(workitem_id, action, kwargs)
        return {'scheduled': True, 'backend': 'celery'}

    def schedule_notification(self, user_id, workitem_ids=None):
        from goflow.runtime import tasks

        tasks.notification_task.delay(user_id, workitem_ids)
        return {'scheduled': True, 'backend': 'celery'}


def get_scheduler_backend():
    backend_path = getattr(
        settings,
        'GOFLOW_SCHEDULER_BACKEND',
        'goflow.runtime.scheduler.CronSchedulerBackend',
    )
    backend_class = import_string(backend_path)
    return backend_class()


def schedule_timeout_scan():
    return get_scheduler_backend().schedule_timeout_scan()


def schedule_workitem_action(workitem_id, action='forward', **kwargs):
    return get_scheduler_backend().schedule_workitem_action(
        workitem_id=workitem_id,
        action=action,
        **kwargs,
    )


def schedule_notification(user_id, workitem_ids=None):
    return get_scheduler_backend().schedule_notification(
        user_id=user_id,
        workitem_ids=workitem_ids,
    )
