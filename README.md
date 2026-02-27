# Historic links

* https://code.djangoproject.com/wiki/GoFlow:demo 
* http://goflow.free.fr/doc/html/install.html#optional-but-useful-modules

This is django-goflow migrated from django 1.X to modern Django versions.

Release 1.1 highlights (2026-02-27):

- Added pluggable scheduler backends (cron/celery).
- Replaced eval/exec in key runtime paths with safe condition parsing.
- Updated automation/admin/designer documentation.

Current compatibility target:

- Django 4.2.x
- Django 5.x
- Django 6.x
- Python 3.9+

Compatibility matrix:

- Python 3.9: Django 4.2
- Python 3.10/3.11: Django 4.2, 5.x
- Python 3.12+: Django 4.2, 5.x, 6.x

Use `tox` to run compatibility checks across supported Django versions.

Multilingual support:

- Languages: en, fr, zh-hans, zh-hant, ja, de, es, it
- Switching: URL prefix, session/cookie, or browser Accept-Language

Quick start (sampleproject):

1) Create venv and install dependencies.
2) Run migrations:

	python sampleproject/manage.py migrate

3) Create a superuser:

	python sampleproject/manage.py createsuperuser

4) Run the server:

	python sampleproject/manage.py runserver

5) Open:

	http://localhost:8000/admin/
	http://localhost:8000/workflow/
	http://localhost:8000/workflow/designer/<process_id>/

Quick start (leavedemo):

1) Run migrations:

	python leavedemo/manage.py migrate

2) Run the server:

	python leavedemo/manage.py runserver

3) Open:

	http://localhost:8000/leave/admin/
	http://localhost:8000/leave/
	http://localhost:8000/leave/designer/<process_id>/

Language switching:

- URL prefix example: /en/leave/ or /zh-hans/leave/
- POST to /i18n/setlang/ with "language" to set session/cookie
- To generate translations:

  django-admin makemessages -a
  django-admin compilemessages

Roles and permissions:

- Disable automatic process group creation (use Django auth to manage roles):
	GOFLOW_AUTO_CREATE_PROCESS_GROUPS = False

Scheduling backends (pluggable):

- Default backend (linux cron + management command):
	GOFLOW_SCHEDULER_BACKEND = 'goflow.runtime.scheduler.CronSchedulerBackend'
- Optional Celery backend:
	GOFLOW_SCHEDULER_BACKEND = 'goflow.runtime.scheduler.CelerySchedulerBackend'

Public scheduler interfaces:

- `schedule_timeout_scan()`
- `schedule_workitem_action(workitem_id, action='forward', **kwargs)`
- `schedule_notification(user_id, workitem_ids=None)`

Cron command:

- `python manage.py goflow_cron`

Transition condition syntax (safe parser):

- `eq:APPROVED`
- `ne:REJECTED`
- `in:APPROVED,OK`
- `notin:REJECTED,CANCELLED`
- `timeout:3d`
- `instance.condition == 'APPROVED'`

Condition strategy:

- `GOFLOW_CONDITION_STRATEGY = 'compatible'` (default): unknown expressions fall back to legacy `instance.condition == raw_text`.
- `GOFLOW_CONDITION_STRATEGY = 'strict'`: unknown/invalid expressions evaluate to `False`.

Condition normalization:

- On transition save, plain values are normalized automatically:
	- `APPROVED` -> `eq:APPROVED`
	- `workitem.time_out(3, unit='days')` -> `timeout:3d`

Docs build:

- HTML docs:
	python -m sphinx -b html -d docs/build/doctrees docs/source docs/build/html

REST API (django-ninja + django-ninja-simple-jwt):

- Install deps: django-ninja, django-ninja-simple-jwt
- Generate JWT keys (dev only):

	python sampleproject/manage.py make_rsa

- Auth endpoints:
	/api/auth/mobile/sign-in
	/api/auth/mobile/token-refresh
	/api/auth/web/sign-in
	/api/auth/web/token-refresh

- Auth example (web):

```bash
curl -X POST http://localhost:8000/api/auth/web/sign-in \
  -H "Content-Type: application/json" \
  -d '{"username":"admin","password":"open"}'
```

```json
{"access":"<jwt>"}
```

The refresh token is set in an HttpOnly cookie named `refresh`.

- Token refresh:

```bash
curl -X POST http://localhost:8000/api/auth/web/token-refresh \
	--cookie "refresh=<jwt>"
```

```json
{"access":"<jwt>"}
```

- Auth example (mobile):

```bash
curl -X POST http://localhost:8000/api/auth/mobile/sign-in \
	-H "Content-Type: application/json" \
	-d '{"username":"admin","password":"open"}'
```

```json
{"access":"<jwt>","refresh":"<jwt>"}
```

- Protected example:

```bash
curl http://localhost:8000/api/protected/me \
  -H "Authorization: Bearer <jwt>"
```

```json
{"username":"admin","is_authenticated":true}
```

- Workflow resources (JWT required):
	/api/protected/processes
	/api/protected/processes/{process_id}/activities
	/api/protected/workitems
	/api/protected/my/workitems
	/api/protected/workitems/{id}/activate
	/api/protected/workitems/{id}/complete
	/api/protected/processes/start

- List processes:

```bash
curl http://localhost:8000/api/protected/processes \
  -H "Authorization: Bearer <jwt>"
```

```json
[{"id":1,"title":"leave","enabled":true}]
```

- List activities for a process:

```bash
curl http://localhost:8000/api/protected/processes/1/activities \
  -H "Authorization: Bearer <jwt>"
```

```json
[{"id":1,"title":"Start","kind":"standard","process_id":1}]
```

- List all workitems:

```bash
curl http://localhost:8000/api/protected/workitems \
  -H "Authorization: Bearer <jwt>"
```

```json
[{"id":1,"status":"active","activity_id":2,"instance_id":1,"user_id":1}]
```

- List my workitems:

```bash
curl http://localhost:8000/api/protected/my/workitems \
  -H "Authorization: Bearer <jwt>"
```

```json
[{"id":1,"status":"active","activity_id":2,"instance_id":1,"user_id":1}]
```

- Activate a workitem:

```bash
curl -X POST http://localhost:8000/api/protected/workitems/1/activate \
  -H "Authorization: Bearer <jwt>"
```

```json
{"status":"activated","workitem_id":1}
```

- Complete a workitem:

```bash
curl -X POST http://localhost:8000/api/protected/workitems/1/complete \
  -H "Authorization: Bearer <jwt>" \
  -H "Content-Type: application/json" \
  -d '{"condition":"APPROVED"}'
```

```json
{"status":"completed","workitem_id":1}
```

- Start a process instance:

```bash
curl -X POST http://localhost:8000/api/protected/processes/start \
  -H "Authorization: Bearer <jwt>" \
  -H "Content-Type: application/json" \
	-d '{"process_name":"leave","content_app_label":"leave","content_model":"leaverequest","object_id":1,"title":"Vacation request","priority":5}'
```

```json
{"status":"started","workitem_id":12,"instance_id":9}
```

- Error responses:
  - 401/403: missing or invalid token
  - 403: process or content type not allowed
	- 403: object not allowed
  - 400: invalid content type
  - 404: content object not found

- Schema summary:

SignInRequest

| Field | Type | Notes |
| --- | --- | --- |
| username | string | Required |
| password | string | Required |

WebSignInResponse

| Field | Type | Notes |
| --- | --- | --- |
| access | string | JWT access token |

MobileSignInResponse

| Field | Type | Notes |
| --- | --- | --- |
| access | string | JWT access token |
| refresh | string | JWT refresh token |

ProcessOut

| Field | Type | Notes |
| --- | --- | --- |
| id | integer | Process ID |
| title | string | Process title |
| enabled | boolean | Enabled flag |

ActivityOut

| Field | Type | Notes |
| --- | --- | --- |
| id | integer | Activity ID |
| title | string | Activity title |
| kind | string | Activity kind |
| process_id | integer | Process ID |

WorkItemOut

| Field | Type | Notes |
| --- | --- | --- |
| id | integer | Work item ID |
| status | string | Work item status |
| activity_id | integer | Activity ID |
| instance_id | integer | Process instance ID |
| user_id | integer or null | Assigned user ID |

StartProcessIn

| Field | Type | Notes |
| --- | --- | --- |
| process_name | string | Process title |
| content_app_label | string | Django app label |
| content_model | string | Model name (lowercase) |
| object_id | integer | Object primary key |
| title | string or null | Optional instance title |
| priority | integer or null | Optional priority |

StartProcessResponse

| Field | Type | Notes |
| --- | --- | --- |
| status | string | "started" |
| workitem_id | integer | First work item ID |
| instance_id | integer | Process instance ID |

- Optional API access controls (settings.py):

```python
GOFLOW_API_ALLOWED_PROCESS_TITLES = ("leave", "Gestion des absences")
GOFLOW_API_ALLOWED_CONTENT_TYPES = ("leave.leaverequest",)
GOFLOW_API_REQUIRE_OBJECT_OWNERSHIP = True
GOFLOW_API_OBJECT_OWNER_FIELDS = ("requester",)
```

- Sampleproject note:
	- Process titles: "Sample process", "test parallel workflow"
	- Content type: "sampleapp.samplemodel"

Advanced example (summary):

- Parallel reviews: set ``approve.split_mode = 'and'`` and add
	``security_review`` and ``finance_review`` activities, both leading to
	``finalize`` with ``finalize.join_mode = 'and'``.
- Timeout transition: add a transition with condition
	``workitem.time_out(3, unit='days')`` and run ``goflow_cron`` to forward.
- Exception path: set ``instance.condition = 'EXCEPTION'`` and transition to
	``exception_review`` for manual recovery.

Leave demo data:

- PostgreSQL backup: leavedemo/pgdb/leavedemo20180517.backup
- SQLite fallback: sampleprojectdata.sqlite3

