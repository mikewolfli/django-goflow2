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

These partials are optional and can be customized per project.
