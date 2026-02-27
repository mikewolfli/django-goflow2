API Guide
=========

Overview
--------

GoFlow ships REST endpoints via django-ninja and django-ninja-simple-jwt.
The API is mounted at /api/ for both sampleproject and leavedemo.

Authentication
--------------

Generate JWT keys (dev only):

.. code-block:: bash

   python manage.py make_rsa

Sign in (web):

.. code-block:: bash

   curl -X POST http://localhost:8000/api/auth/web/sign-in \
     -H "Content-Type: application/json" \
     -d '{"username":"admin","password":"open"}'

.. code-block:: json

   {"access":"<jwt>"}

The refresh token is set in an HttpOnly cookie named ``refresh``.

Ownership checks resolve JWT token users to real Django users by ID,
so the user must exist in the database.

Refresh token (web):

.. code-block:: bash

    curl -X POST http://localhost:8000/api/auth/web/token-refresh \
       --cookie "refresh=<jwt>"

.. code-block:: json

   {"access":"<jwt>"}

Sign in (mobile):

.. code-block:: bash

   curl -X POST http://localhost:8000/api/auth/mobile/sign-in \
     -H "Content-Type: application/json" \
     -d '{"username":"admin","password":"open"}'

.. code-block:: json

   {"access":"<jwt>","refresh":"<jwt>"}

Get current user:

.. code-block:: bash

   curl http://localhost:8000/api/protected/me \
     -H "Authorization: Bearer <jwt>"

.. code-block:: json

   {"username":"admin","is_authenticated":true}

Workflow endpoints
------------------

List processes:

.. code-block:: bash

   curl http://localhost:8000/api/protected/processes \
     -H "Authorization: Bearer <jwt>"

.. code-block:: json

   [{"id":1,"title":"leave","enabled":true}]

List activities for a process:

.. code-block:: bash

   curl http://localhost:8000/api/protected/processes/1/activities \
     -H "Authorization: Bearer <jwt>"

.. code-block:: json

   [{"id":1,"title":"Start","kind":"standard","process_id":1}]

List all workitems:

.. code-block:: bash

   curl http://localhost:8000/api/protected/workitems \
     -H "Authorization: Bearer <jwt>"

.. code-block:: json

   [{"id":1,"status":"active","activity_id":2,"instance_id":1,"user_id":1}]

List my workitems:

.. code-block:: bash

   curl http://localhost:8000/api/protected/my/workitems \
     -H "Authorization: Bearer <jwt>"

.. code-block:: json

   [{"id":1,"status":"active","activity_id":2,"instance_id":1,"user_id":1}]

Activate a workitem:

.. code-block:: bash

   curl -X POST http://localhost:8000/api/protected/workitems/1/activate \
     -H "Authorization: Bearer <jwt>"

.. code-block:: json

   {"status":"activated","workitem_id":1}

Complete a workitem:

.. code-block:: bash

   curl -X POST http://localhost:8000/api/protected/workitems/1/complete \
     -H "Authorization: Bearer <jwt>" \
     -H "Content-Type: application/json" \
     -d '{"condition":"APPROVED"}'

.. code-block:: json

   {"status":"completed","workitem_id":1}

Start a process instance:

.. code-block:: bash

   curl -X POST http://localhost:8000/api/protected/processes/start \
     -H "Authorization: Bearer <jwt>" \
     -H "Content-Type: application/json" \
     -d '{"process_name":"leave","content_app_label":"leave","content_model":"leaverequest","object_id":1,"title":"Vacation request","priority":5}'

.. code-block:: json

   {"status":"started","workitem_id":12,"instance_id":9}

Error responses
---------------

- 401/403: missing or invalid token
- 403: process or content type not allowed
- 400: invalid content type
- 404: content object not found

Access control settings
-----------------------

Restrict which processes and content types can be used via API:

.. code-block:: python

   GOFLOW_API_ALLOWED_PROCESS_TITLES = ("leave", "Gestion des absences")
   GOFLOW_API_ALLOWED_CONTENT_TYPES = ("leave.leaverequest",)
  GOFLOW_API_REQUIRE_OBJECT_OWNERSHIP = True
  GOFLOW_API_OBJECT_OWNER_FIELDS = ("requester",)

Sampleproject defaults:

- Process titles: "Sample process", "test parallel workflow"
- Content type: "sampleapp.samplemodel"

Designer layout persistence
---------------------------

The workflow designer stores node positions in the database so the layout
is preserved between sessions.

Schemas
-------

Auth request/response
~~~~~~~~~~~~~~~~~~~~~

.. list-table:: SignInRequest
   :header-rows: 1

   * - Field
     - Type
     - Notes
   * - username
     - string
     - Required
   * - password
     - string
     - Required

.. list-table:: WebSignInResponse
   :header-rows: 1

   * - Field
     - Type
     - Notes
   * - access
     - string
     - JWT access token

.. list-table:: MobileSignInResponse
   :header-rows: 1

   * - Field
     - Type
     - Notes
   * - access
     - string
     - JWT access token
   * - refresh
     - string
     - JWT refresh token

Workflow response schemas
~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table:: ProcessOut
   :header-rows: 1

   * - Field
     - Type
     - Notes
   * - id
     - integer
     - Process ID
   * - title
     - string
     - Process title
   * - enabled
     - boolean
     - Enabled flag

.. list-table:: ActivityOut
   :header-rows: 1

   * - Field
     - Type
     - Notes
   * - id
     - integer
     - Activity ID
   * - title
     - string
     - Activity title
   * - kind
     - string
     - Activity kind
   * - process_id
     - integer
     - Process ID

.. list-table:: WorkItemOut
   :header-rows: 1

   * - Field
     - Type
     - Notes
   * - id
     - integer
     - Work item ID
   * - status
     - string
     - Work item status
   * - activity_id
     - integer
     - Activity ID
   * - instance_id
     - integer
     - Process instance ID
   * - user_id
     - integer or null
     - Assigned user ID

.. list-table:: StartProcessIn
   :header-rows: 1

   * - Field
     - Type
     - Notes
   * - process_name
     - string
     - Process title
   * - content_app_label
     - string
     - Django app label
   * - content_model
     - string
     - Model name (lowercase)
   * - object_id
     - integer
     - Object primary key
   * - title
     - string or null
     - Optional instance title
   * - priority
     - integer or null
     - Optional priority

.. list-table:: StartProcessResponse
   :header-rows: 1

   * - Field
     - Type
     - Notes
   * - status
     - string
     - "started"
   * - workitem_id
     - integer
     - First work item ID
   * - instance_id
     - integer
     - Process instance ID
