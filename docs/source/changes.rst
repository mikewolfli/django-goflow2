.. rst3: filename: changes.rst

.. _changes:

==========
What's new
==========

.. contents::

Release 1.1
+++++++++++

New Features
************

* Added a pluggable scheduler abstraction with three public interfaces:

	* ``schedule_timeout_scan()``
	* ``schedule_workitem_action(workitem_id, action='forward', **kwargs)``
	* ``schedule_notification(user_id, workitem_ids=None)``

* Added two scheduler backends:

	* ``CronSchedulerBackend`` for Linux cron + management command execution.
	* ``CelerySchedulerBackend`` for asynchronous task scheduling.

* Added automation entry points in runtime:

	* ``run_timeout_scan()``
	* ``run_workitem_action()``
	* ``run_user_notification()``

* Added management command ``goflow_cron`` to execute periodic timeout scanning from system cron.

* Added transition condition normalization and safer condition parsing with explicit DSL support:

	* ``eq:``, ``ne:``, ``in:``, ``notin:``, ``timeout:``
	* Restricted expression evaluation without ``eval``/``exec`` in runtime condition paths.

* Added admin and workflow-designer guidance for condition syntax and parameter mapping formats.

Bug Fixes
*********

* Removed ``eval``/``exec`` usage from key workflow execution paths, including:

	* transition condition matching
	* timeout condition detection
	* push application parameter parsing
	* push application handler resolution

* Reworked timeout expression handling to use validated unit mapping instead of dynamic code execution.

* Ensured transition conditions are normalized on save for more consistent behavior across designer/admin/runtime.

* Updated docs to include automation configuration, scheduler backend selection, and condition strategy guidance.

Backwards Incompatible Changes
******************************

* Condition evaluation now defaults to safe parsing behavior.

* Introduced ``GOFLOW_CONDITION_STRATEGY`` setting:

	* ``compatible`` (default): unknown expressions fall back to legacy plain-text comparison behavior.
	* ``strict``: unknown or invalid expressions evaluate to ``False``.

* Introduced ``GOFLOW_SCHEDULER_BACKEND`` setting for selecting cron or celery scheduling backend.

* Added optional dependency group ``django-goflow2[celery]`` for Celery-based scheduling integration.

