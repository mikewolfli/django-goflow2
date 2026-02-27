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
