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
- ``schedule_workitem_action(workitem_id, action='forward', **kwargs)``
- ``schedule_notification(user_id, workitem_ids=None)``

These interfaces are provided in:

.. code-block:: python

   from goflow.runtime.scheduler import (
       schedule_timeout_scan,
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
