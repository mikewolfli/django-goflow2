.. rst3: filename: automation.rst

.. _automation:

=======================================
Automation, Scheduling and Conditions
=======================================

Overview
++++++++

GoFlow supports pluggable automation backends and a safe transition-condition parser.
This allows package users to choose runtime scheduling strategy without coupling the
core engine to a specific queue system.


Scheduler Backends (Pluggable)
+++++++++++++++++++++++++++++++

Set the backend with Django settings:

.. code-block:: python

   GOFLOW_SCHEDULER_BACKEND = 'goflow.runtime.scheduler.CronSchedulerBackend'

or:

.. code-block:: python

   GOFLOW_SCHEDULER_BACKEND = 'goflow.runtime.scheduler.CelerySchedulerBackend'

Built-in backends:

- ``goflow.runtime.scheduler.CronSchedulerBackend``
- ``goflow.runtime.scheduler.CelerySchedulerBackend``


Public Scheduler Interfaces
+++++++++++++++++++++++++++

The following interfaces are stable entry points for automation:

- ``schedule_timeout_scan()``
- ``schedule_sla_scan()``
- ``schedule_workitem_action(workitem_id, action='forward', **kwargs)``
- ``schedule_notification(user_id, workitem_ids=None)``

These interfaces are provided in:

.. code-block:: python

   from goflow.runtime.scheduler import (
       schedule_timeout_scan,
          schedule_sla_scan,
       schedule_workitem_action,
       schedule_notification,
   )


Cron Mode
+++++++++++++++++++++++++++++

For Linux cron usage, GoFlow provides a management command:

.. code-block:: bash

   python manage.py goflow_cron

Suggested crontab example:

.. code-block:: bash

   * * * * * /path/to/venv/bin/python /path/to/project/manage.py goflow_cron


Celery Mode
+++++++++++++++++++++++++++++

Celery backend is optional and can be enabled by setting
``GOFLOW_SCHEDULER_BACKEND`` to ``CelerySchedulerBackend``.

In package mode, this keeps core workflow logic decoupled from broker/runtime choice.


Audit Logging
+++++++++++++++++++++++++++++

GoFlow logs audit events for key runtime actions (process start, workitem
activation/completion, timeout forwarding, SLA warnings and breaches).

Enable/disable audit logging:

.. code-block:: python

   GOFLOW_AUDIT_ENABLED = True

Audit events are stored in ``AuditEvent`` and can optionally trigger webhooks.


SLA and Escalation
+++++++++++++++++++++++++++++

SLA fields are configured per activity:

- ``sla_duration``: breach threshold (e.g. ``3d``)
- ``sla_warn``: warning threshold (e.g. ``2d``)

Enable SLA scanning:

.. code-block:: python

   GOFLOW_SLA_ENABLED = True
   GOFLOW_SLA_NOTIFY = True
   GOFLOW_SLA_AUTO_ASSIGN = False

When enabled, ``goflow_cron`` runs SLA scans in addition to timeout scans.


Process Versioning
+++++++++++++++++++++++++++++

Processes support versions and publishing states. New process instances
start from the latest published version.

Fields:

- ``code``: stable identifier across versions (defaults to title)
- ``version``: incremental version
- ``status``: ``draft``, ``published``, or ``retired``

Publishing flow:

- Use the admin "Publish" action to promote a version.
- Use "Clone" to create a new draft version.
- Compare versions via the diff endpoint in the versions view.


Permissions and Access Control
+++++++++++++++++++++++++++++

Activities support explicit allowlists in addition to roles:

- ``allowed_users``
- ``allowed_groups``

If set, these are checked before role-based access.


Compensation Hooks
+++++++++++++++++++++++++++++

You can configure a compensation handler per activity. This is a callable path
invoked when a workitem falls out (optionally auto-triggered via settings).

.. code-block:: python

   GOFLOW_COMPENSATION_AUTO = False

Compensation handler example:

.. code-block:: python

   # path: goflow.runtime.compensation.compensate_refund
   def compensate_refund(workitem, reason=None):
      return True


Webhook Integrations
+++++++++++++++++++++++++++++

Audit events can trigger webhook deliveries to external systems.

.. code-block:: python

   GOFLOW_WEBHOOK_ENABLED = True
   GOFLOW_WEBHOOK_TIMEOUT = 5

Webhook endpoints are managed via ``WebhookEndpoint`` model in the admin.

Tenant/Org extension hooks (optional):

- ``GOFLOW_TENANT_RESOLVER``: callable returning ``{"tenant_id": ..., "org_id": ...}``
- ``GOFLOW_TENANT_FILTER``: callable for scoping querysets

Test webhook delivery:

.. code-block:: bash

   python manage.py goflow_webhook_test --action test.ping

Example payload (JSON):

.. code-block:: json

    {
       "id": 123,
       "action": "test.ping",
       "created_at": "2026-02-27T14:35:00+00:00",
       "actor_id": null,
       "process_id": null,
       "instance_id": null,
       "workitem_id": null,
       "activity_id": null,
       "transition_id": null,
       "status_from": null,
       "status_to": null,
       "metadata": {
          "test": true
       }
    }


Safe Transition Conditions
+++++++++++++++++++++++++++++

Transition conditions are parsed without ``eval`` and support a compact DSL.

Recommended formats:

- ``eq:APPROVED``
- ``ne:REJECTED``
- ``in:APPROVED,OK``
- ``notin:REJECTED,CANCELLED``
- ``timeout:3d``

Safe expression mode is also supported for simple comparisons, for example:

- ``instance.condition == 'APPROVED'``


Condition Strategy
+++++++++++++++++++++++++++++

Set behavior for unknown/invalid conditions:

.. code-block:: python

   GOFLOW_CONDITION_STRATEGY = 'compatible'  # default

or:

.. code-block:: python

   GOFLOW_CONDITION_STRATEGY = 'strict'

Behavior:

- ``compatible``: fallback to legacy equality check against ``instance.condition``
- ``strict``: invalid/unknown expressions evaluate to ``False``


Condition Normalization
+++++++++++++++++++++++++++++

On transition save, GoFlow normalizes condition text:

- ``APPROVED`` -> ``eq:APPROVED``
- ``workitem.time_out(3, unit='days')`` -> ``timeout:3d``

This normalization applies to both admin edits and workflow designer saves.
