.. rst3: filename: install.rst

.. _install:

==================
Installation
==================

    
Python
-------

Python 3.9+ is required. Use your platform package manager or https://www.python.org.
      

Django
------

Supported Django versions: 4.2, 5.x, 6.x.
    
    
GoFlow
-------

Latest Release: 
    
    * All releases are available here: http://code.google.com/p/goflow/downloads/list
    
Subversion trunk code::
    
    svn checkout http://goflow.googlecode.com/svn/trunk/ goflow-src
    

  
Optional (but useful) Modules      
-------------------------------

    * Graphviz
    * PIL  
    * Pyyaml
    * Pygraphviz

Internationalization (i18n)
---------------------------

Supported languages: en, fr, zh-hans, zh-hant, ja, de, es, it.

Language switching options:

- URL prefix via ``i18n_patterns``
- Session/cookie via ``LocaleMiddleware``
- Browser ``Accept-Language``


Automation Quick Configuration
------------------------------

GoFlow automation can run with pluggable backends.

Default (linux cron + management command):

.. code-block:: python

    GOFLOW_SCHEDULER_BACKEND = 'goflow.runtime.scheduler.CronSchedulerBackend'
    GOFLOW_CONDITION_STRATEGY = 'compatible'

Run periodic automation:

.. code-block:: bash

    python manage.py goflow_cron

Optional Celery backend:

.. code-block:: python

    GOFLOW_SCHEDULER_BACKEND = 'goflow.runtime.scheduler.CelerySchedulerBackend'

Install optional dependency:

.. code-block:: bash

    pip install django-goflow2[celery]


