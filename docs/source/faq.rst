.. rst3: filename: faq.rst

.. _faq:


============
GoFlow FAQ
============

What is this all about?
+++++++++++++++++++++++

To understand what is ``activity based workflow`` take a look at `OpenFlow`_ 

.. _OpenFlow: http://www.openflow.it/Documentation/documentation/OpenFlowIntroduction

When should I use PushApplication and when should I use Roles in Activity definition? What happens if I select both?
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

When an Activity is activated (automatically or manually by calling activate API method) it is assigned to the User that is returned by PushApplication. If there is no PushApplication then Activity is assigned to selected Roles. If you choose both, then only PushApplication is used.

What are AutoStart and AutoFinish in Activity definition
++++++++++++++++++++++++++++++++++++++++++++++++++++++++

AutoStart and AutoFinish are start mode and finish mode as described here: http://www.openflow.it/Documentation/documentation/OpenFlowIntroduction For example if AutoStart is not checked, then to start Activity it is necessary to call activate API function on it. If AutoStart is checked, then it is automatically activated as soon as previous activities are finished (depending on guard condition: xor, and)

How should I define a transition condition ?
++++++++++++++++++++++++++++++++++++++++++++

Transitions have a condition attribute evaluated by a safe parser. You can use a compact DSL or a simple expression. The variables available are ``instance`` and ``workitem``. Examples:

    * eq:OK - the user has pushed the OK button
    * instance.condition == "OK" - the user has pushed the OK button
    * timeout:5d - the task is waiting for 5 days or more
    * workitem.time_out(delay=5, unit='days') - equivalent to ``timeout:5d``

Related settings and behavior:

    * ``GOFLOW_CONDITION_STRATEGY = 'compatible'`` (default): unknown/invalid expressions fall back to legacy equality check against ``instance.condition``.
    * ``GOFLOW_CONDITION_STRATEGY = 'strict'``: unknown/invalid expressions evaluate to ``False``.
    * Timeout conditions are enforced by running the ``goflow_cron`` management command periodically.

Is it valid to reuse Activities?
++++++++++++++++++++++++++++++++

The good practise is to reuse Applications, not Activities: Applications should be reused because they take time to build; Activities are just containers for applications, with some parameters to fit the process needs.

You can customize application with parameters:

    * at global level, in urls.py files
    * at process level, in activities (application parameters field)

