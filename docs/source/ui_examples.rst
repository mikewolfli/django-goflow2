.. rst3: filename: ui_examples.rst

.. _ui_examples:

====================
UI Examples
====================

Sample Task Form
----------------

This template demonstrates how to compose the task header, actions, and styles.

.. code-block:: django

   {% extends "admin/base_site.html" %}
   {% block coltype %}colMS{% endblock %}

   {% block content %}
   {% include "goflow/components/task_styles.html" %}

   <div class="module">
     {% include "goflow/components/task_header.html" with title="Sample Task" subtitle="Request #123" %}
    {% include "goflow/components/task_meta.html" with label="Priority" value="Urgent" %}
    {% include "goflow/components/task_notice.html" with tone="warning" message="Needs review" %}

     <form method="post">
       {% csrf_token %}
       <p>
         <label for="id_comment">Comment</label><br />
         <textarea id="id_comment" name="comment" rows="4" cols="50"></textarea>
       </p>
       {% include "goflow/components/task_actions.html" with primary_label="Approve" secondary_label="Reject" %}
     </form>
   </div>
   {% endblock %}

Designer Modeling Example
-------------------------

Recommended setup for advanced node types in the workflow designer:

- ``gateway`` activity:

  - ``kind=dummy``
  - no ``form_template`` / ``form_class``

- ``script`` activity:

  - ``autostart=true``
  - ``autofinish=true``

- ``service`` activity:

  - ``autostart=true``

If these constraints are not met, the designer save API returns explicit validation errors.
