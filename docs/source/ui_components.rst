.. rst3: filename: ui_components.rst

.. _ui_components:

====================
UI Components
====================

GoFlow ships light-weight template partials to standardize task views.
You can include these in your own templates.

Task Header
-----------

.. code-block:: django

   {% include "goflow/components/task_header.html" with title="Approve" subtitle="Request #123" %}

Optional styles:

.. code-block:: django

   {% include "goflow/components/task_styles.html" %}

Task Actions
------------

.. code-block:: django

   {% include "goflow/components/task_actions.html" with primary_label="Approve" secondary_label="Reject" %}

Task Notice
-----------

.. code-block:: django

   {% include "goflow/components/task_notice.html" with tone="warning" message="Needs review" %}

Task Meta
---------

.. code-block:: django

   {% include "goflow/components/task_meta.html" with label="Priority" value="Urgent" %}

These partials are optional and can be customized per project.

Workflow Designer Node Types
----------------------------

The workflow designer displays different node types with distinct shapes:

- ``standard`` / ``approval`` / ``review`` / ``notification``: rounded rectangle
- ``service``: hexagon
- ``gateway``: diamond
- ``script``: cut rectangle

Modeling validation rules in designer save endpoint:

- ``gateway`` nodes must use ``kind=dummy``
- ``gateway`` nodes cannot use ``form_template`` or ``form_class``
- ``service`` and ``script`` nodes should enable ``autostart``
- ``script`` nodes should enable ``autofinish``
- ``notification`` nodes should not use ``form_class``
