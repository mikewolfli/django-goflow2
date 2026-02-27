.. rst3: filename: developer.rst

.. _developer:

=================
Developer Guide
=================

Extension Points
----------------

Signals
^^^^^^^

GoFlow emits signals for workflow lifecycle events. Import from:

.. code-block:: python

   from goflow.runtime import signals

Available signals:

- ``process_started``
- ``process_published``
- ``workitem_created``
- ``workitem_assigned``
- ``workitem_activated``
- ``workitem_completed``
- ``workitem_forwarded``
- ``workitem_blocked``
- ``workitem_fallout``
- ``sla_warned``
- ``sla_breached``
- ``audit_event_created``

Example receiver:

.. code-block:: python

   from django.dispatch import receiver
   from goflow.runtime import signals

   @receiver(signals.workitem_completed)
   def on_workitem_completed(sender, workitem=None, actor=None, **kwargs):
       # your custom logic here
       pass

Scheduler Backend
^^^^^^^^^^^^^^^^^

Provide a custom scheduler backend by implementing:

- ``schedule_timeout_scan``
- ``schedule_sla_scan``
- ``schedule_workitem_action``
- ``schedule_notification``

Then point ``GOFLOW_SCHEDULER_BACKEND`` to your class.

Webhook Integrations
^^^^^^^^^^^^^^^^^^^^

Audit events can trigger webhooks when ``GOFLOW_WEBHOOK_ENABLED`` is True.
Use ``WebhookEndpoint`` in admin to register URLs.

Compensation Handlers
^^^^^^^^^^^^^^^^^^^^^

Define a callable and reference it in activity ``compensation_handler``.
Example:

.. code-block:: python

   def compensate_refund(workitem, reason=None):
       return True

Tenant/Org Hooks
^^^^^^^^^^^^^^^^

Optional hooks for tenant scoping:

- ``GOFLOW_TENANT_RESOLVER``: returns ``{"tenant_id": ..., "org_id": ...}``
- ``GOFLOW_TENANT_FILTER``: scopes queryset based on current context
