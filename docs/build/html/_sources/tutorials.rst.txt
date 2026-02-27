.. rst3: filename: tutorials.rst

.. _tutorial:

==================
GoFlow User Guide
==================

GoFlow is a `django component` which adds activity-based workflow features to a django project.

We'll learn here how to use this module, starting with a very simple "Hello world" django project, and then gradually add features as we go along.

Prerequisites
+++++++++++++

Prerequisite
=================
Create a directory, and copy the directory ``goflow`` to this directory (you can also place it in any directory in your PYTHONPATH).

.. note::
   While the Django documentation advocates the use of absolute paths, the use of relative paths
   in what follows is voluntary. This is done in order to simplify expressions and to be platform 
   independent (and it works, at least under Windows and OS X)

Project "Hello World"
+++++++++++++++++++++

Project "Hello World"
======================
We will discover the workflow engine with a very simple application based on a process workflow with a single activity (a single activity, with no transitions: the simplest possible workflow). The purpose of this activity is to receive a message (for example, "Hello world").

    * Start by creating an empty django project (or use an existing project)::

      django-admin startproject myproj

    * Add the following applications in the file ``settings.py``::

        INSTALLED_APPS = (
         ...
         'django.contrib.admin',
         'django.contrib.auth',
         'django.contrib.contenttypes',
         'django.contrib.sessions',
         'django.contrib.messages',
         'django.contrib.staticfiles',
         'goflow.workflow',
         'goflow.runtime',
         'goflow.apptools',
        )

The `workflow` application contains the "static" model data (modeling
process), and the ``instances`` application contains the dynamic part or runtime.

    * Set up the database part of the settings file, for example like this::

      DATABASES = {
        'default': {
          'ENGINE': 'django.db.backends.sqlite3',
          'NAME': 'data.sqlite3',
        }
      }

    * Add the following lines in the ``urls.py`` file::

      from django.contrib import admin
      from django.urls import path, include

      urlpatterns = [
        path('admin/', admin.site.urls),
        path('workflow/', include('goflow.urls')),
      ]


    * Now create the database server and start it as follows::

      python manage.py migrate
      python manage.py runserver


We can now open the console admin [http://localhost:8000/admin/], and discover the data models introduced by GoFlow:

..  image:: images/admin1.png
    :align: center

We can also discover the GoFlow Dashboard, which provide easy access to the status of workflows using a "back-office" perspective, [http://localhost:8000/workflow/]

..  image:: images/admin2.png
    :align: center

We will now create a process workflow.

Return to the admin console, add an entity Process as shown with the screen below:

..  image:: images/admin4.png
    :align: center

Use "Hello world" for the title, and optionally provide a description of the new process

    * Register using the ``Save button and continue editing``: you can now see that an 
      activity ``End`` was added automatically.

    * Create an initial activity by clicking on the icon "+" in the field ``Initial activity``: 
      enter a title, set the process dropdown to the current process "Hello world", leaving the 
      default values for other fields.

    * Save

We have created our first process workflow:

..  image:: images/admin4.png
    :align: center

You may observe that we have not yet specified an application (a url with underlying functionality e.g. views/templates/classes/functions/modules etc..) for our business, and we will shortly see that this is not necessary to begin to "play" with our application.

Indeed, when an activity is not associated with an application, a special testing application is still invoked to simulate this activity: providing a panel to the user, displaying the name, description of the activity, and also a history of the workflow, with an ``OK`` button allowing you to complete the activity.

Before we start running our process workflow, we must first create a ``Group`` with a single permission to allow users to instantiate it:

    * Add a group named ``Hello world``, give it the permission ``can_instantiate`` on the  
      content type ``workflow.process``, and save. (note: the name of the group and the name of 
      the process must be the same)
      
    * Add this group to the current user: this will allow the user to instantiate the process 
      ``Hello world``.

We are now ready to execute/test the workflow: go to the dashboard [http://localhost:8000/workflow/]. You will find the process and its definition, and other information on roles and permissions.

Internationalization (optional)
******************************

If you enable i18n URL prefixes, you can visit /en/ or /zh-hans/ and so on.
You can also POST to /i18n/setlang/ with the "language" field to persist
the language in session/cookies.

    * Click on the link ``start a simulation instance`` under the process ``Hello world``

Let's add an activity
*********************

Let's add our own models
************************

Create a small model for a workflow-backed request. In your app's
``models.py``::

  from django.db import models
  from django.conf import settings
  from django.utils.translation import gettext_lazy as _

  class Request(models.Model):
    title = models.CharField(max_length=120, verbose_name=_('title'))
    body = models.TextField(verbose_name=_('body'))
    requester = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
      return self.title

And for some code
*****************

We will implement a form and a view that starts a workflow instance.

In ``forms.py``::

  from django import forms
  from django.utils.translation import gettext_lazy as _
  from .models import Request

  class RequestForm(forms.ModelForm):
    class Meta:
      model = Request
      fields = ('title', 'body')
      labels = {
        'title': _('title'),
        'body': _('body'),
      }

In ``views.py``::

  from django.shortcuts import render, redirect
  from django.contrib.auth.decorators import login_required
  from .forms import RequestForm
  from goflow.runtime.models import ProcessInstance

  @login_required
  def start_request(request):
    if request.method == 'POST':
      form = RequestForm(request.POST)
      if form.is_valid():
        obj = form.save(commit=False)
        obj.requester = request.user
        obj.save()
        ProcessInstance.objects.start('request', request.user, obj, title=obj.title)
        return redirect('request_done')
    else:
      form = RequestForm()
    return render(request, 'request/start.html', {'form': form})

In ``urls.py``::

  from django.urls import path
  from . import views

  urlpatterns = [
    path('request/start/', views.start_request, name='request_start'),
    path('request/done/', views.done, name='request_done'),
  ]

Template ``templates/request/start.html``::

  <h1>{% trans "Start Request" %}</h1>
  <form method="post">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">{% trans "Submit" %}</button>
  </form>

Internationalization checklist
******************************

- Wrap user-facing strings with ``gettext_lazy`` or ``{% trans %}``.
- Run ``django-admin makemessages -a`` and ``compilemessages``.
- Use ``/i18n/setlang/`` or URL prefixes to switch language.

Process modeling, roles, and auto tasks
======================================

This section shows a complete example of:

- modeling a process with manual and automatic activities
- assigning roles and permissions
- verifying auto tasks run without user intervention

1) Create a process and activities
----------------------------------

In the Django admin:

- Create a ``Process`` named ``request``.
- Create an ``Activity`` named ``submit`` (kind=standard, join=xor, split=xor).
- Create an ``Activity`` named ``approve`` (kind=standard).
- Create an ``Activity`` named ``notify`` (kind=standard, autostart=True).
- Set ``submit`` as begin activity and ``notify`` as end activity.

2) Create transitions
---------------------

Create transitions:

- ``submit -> approve`` with condition ``instance.condition == 'OK'``
- ``approve -> notify`` with condition ``instance.condition == 'OK'``

3) Define roles and permissions
-------------------------------

Create two groups and assign permissions:

- Group ``request`` with permission ``workflow.can_instantiate``
- Group ``approver`` with permission ``workflow.can_instantiate``

Assign activity roles:

- ``submit``: group ``request``
- ``approve``: group ``approver``

Add users to those groups in the admin.

4) Wire activity applications
-----------------------------

Register two application URLs:

- ``request/start`` for the submit activity
- ``request/approve`` for the approve activity

Then, set these URLs in the ``Activity`` application field.

5) Implement the approve view
-----------------------------

In ``views.py``::

  from django.contrib.auth.decorators import login_required
  from django.shortcuts import render, redirect
  from goflow.runtime.models import WorkItem

  @login_required
  def approve_request(request, id):
    workitem = WorkItem.objects.get_safe(id=id, user=request.user)
    if request.method == 'POST':
      workitem.instance.condition = 'OK'
      workitem.instance.save()
      workitem.complete(request.user)
      return redirect('request_done')
    return render(request, 'request/approve.html', {'workitem': workitem})

6) Implement the auto task
--------------------------

Define an auto application (no UI) for ``notify``. It can send an email and
then complete automatically. In ``views.py``::

  from django.core.mail import send_mail

  def notify_request(workitem=None, **kwargs):
    if not workitem:
      return
    send_mail(
      subject='Request approved',
      message='Your request was approved.',
      from_email=None,
      recipient_list=[workitem.user.email],
      fail_silently=True,
    )

The workflow runtime will call this when the ``notify`` activity is reached
because it is marked ``autostart=True``.

7) Verify the flow
------------------

- Login as a user in the ``request`` group and start a request.
- Login as a user in the ``approver`` group and approve it.
- The ``notify`` activity runs automatically; check logs or email output.

Parallel branches, timeouts, and rollback
========================================

This section extends the example to include:

- parallel branches (split_mode=and)
- timeout-driven transitions
- rollback/exception handling

1) Add a parallel review branch
-------------------------------

Create two new activities:

- ``security_review`` (kind=standard)
- ``finance_review`` (kind=standard)

Update the ``approve`` activity:

- set ``split_mode`` to ``and``

Add transitions:

- ``approve -> security_review`` with condition ``instance.condition == 'OK'``
- ``approve -> finance_review`` with condition ``instance.condition == 'OK'``

Create a new join activity:

- ``finalize`` (kind=standard, join_mode=and)

Add transitions:

- ``security_review -> finalize``
- ``finance_review -> finalize``

This configuration forces both reviews to complete before ``finalize`` runs.

2) Add timeout handling
-----------------------

Add a transition from ``finance_review`` to ``finalize`` with a timeout condition:

- condition: ``workitem.time_out(3, unit='days')``

Then add a scheduled call to the ``cron`` endpoint or run the cron helper
periodically to forward timed-out workitems.

3) Rollback / exception handling
--------------------------------

When an activity cannot be completed, you can mark the workitem as fallout
and route it to a recovery activity:

- Create ``exception_review`` activity
- Add transition ``finance_review -> exception_review`` with a custom
  condition (e.g. ``instance.condition == 'EXCEPTION'``)

In the review view, set ``instance.condition = 'EXCEPTION'`` and call
``workitem.complete(request.user)`` to route into the exception path.

4) Operational checklist
------------------------

- Verify parallel branches both complete before ``finalize``.
- Trigger a timeout condition and run cron.
- Trigger the exception path and confirm fallback behavior.

Advanced Tutorial
+++++++++++++++++

GoFlow Advanced
============================

Prerequisites
*************

* use goflow svn version as version 0.5 will not work with these tutorials. You can also 
      download the [http://goflow.googlecode.com/files/goflow-0.51.zip v 0.51].
  
    * It is helpful to have a "played" with the demo goflow leave (available online). 
      [http://goflow.alwaysdata.net/leave/]

(tutorial draft; screenshots will be added later)

Application Unit Testing
************************

We will simulate here coding an existing application of the demo ``Leave``: ``hrform``.

    * Launch the local server of the demo ``leave`` in the ``leavedemo`` folder (cf. INSTALL.TXT 
      file)
  
    * Go to the admin console: [http://localhost:8000/leave/admin/]
  
    * Create a !LeaveRequest object: [http://localhost:8000/leave/admin/leave/leaverequest/add/]
        * This object will be used as a model when performing unit tests; hence provide the 
          beginning and end dates, type of absence, the requester (admin), and the reason (e.g 
          "test")
          
    * On the applications panel: [http://localhost:8000/leave/admin/workflow/application/]
    
        * Click on the ``create unit test`` link in the ``hrform`` application row: this will 
          create a process with a single activity that will run the application ``hrform``.
          
        * Click on ``return``
        
        * Click  on the ``start test forums`` link in the ``hrform`` application row; then choose 
          the content type ``leave request`` and click ``OK``: this will initiate as many 
          workflow instances as !LeaveRequest instances that we manually manually before (here, 
          only one).
          
    * Go to the task list of the admin user: [http://localhost:8000/leave/mywork/]
    
    * There must be a task for an activity called ``test_activity`` in the workflow process 
      ``test_hrform``
      
    * Clicking on the link ``activate`` should lead you to the panel corresponding to the 
      implementation of the ``hrform`` application.

Here we have simulated/tested an application in a process workflow; it seems very little, but it is important to have in mind that in the development of complex workflows, and in order to efficiently work in teams, each activity should be coded and tested independently of each other. 

That is why GoFlow is equipped with tools, available in the console admin customized for this purpose, to help the developer generate a test environment for each application.

Application Automation
**********************

We are going to replace an application that currently requires human intervention by an automatic activity. We will work on the previous application ``hrform`` and replace it with the application ``hr_auto`` which will perform the same function but automatically (in fact, this is a simplified version, because calculating the number of days worked between two dates is not trivial).
 
TODO

