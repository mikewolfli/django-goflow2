# Django settings for sampleproject project.
from os.path import dirname, join
from django.utils.translation import gettext_lazy as _
_dir = dirname(__file__)

LIB_PATH = join(_dir,'..')
import sys
sys.path.append(LIB_PATH)

DEBUG = True

ADMINS = (
    # ('Your Name', 'your_email@domain.com'),
)

MANAGERS = ADMINS

DATABASES = {
    # 'default': {
    #     'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
    #     # 'NAME': os.path.join(SITE_ROOT, 'Database') + '/WBDAP.db', # Or path to database file if using sqlite3.
    #     'NAME': os.path.join(SITE_ROOT) + '/WBDAP.db', # Or path to database file if using sqlite3.
    #     'USER': '', # Not used with sqlite3.
    #     'PASSWORD': '', # Not used with sqlite3.
    #     'HOST': '', # Set to empty string for localhost. Not used with sqlite3.
    #     'PORT': '', # Set to empty string for default. Not used with sqlite3.
    #
    #     # 'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
    #     # 'NAME': 'WBDAP', # Or path to database file if using sqlite3.
    #     # 'USER': 'WBDAP', # Not used with sqlite3.
    #     # 'PASSWORD': 'WBDAP', # Not used with sqlite3.
    #     # 'HOST': 'dbserver', # Set to empty string for localhost. Not used with sqlite3.
    #     # 'PORT': '54345', # Set to empty string for default. Not used with sqlite3.
    #
    # },
    #


    'default': {
        # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'ENGINE': 'django.db.backends.sqlite3',
        # 'NAME': os.path.join(SITE_ROOT, 'Database') + '/WBDAP.db', # Or path to database file if using sqlite3.
        # Or path to database file if using sqlite3.
        'NAME': join(_dir) + 'data.sqlite3',
        'USER': '',  # Not used with sqlite3.
        'PASSWORD': '',  # Not used with sqlite3.
        # Set to empty string for localhost. Not used with sqlite3.
        'HOST': '',
        'PORT': '',  # Set to empty string for default. Not used with sqlite3.
    },
}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/Chicago'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True
DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'

LOCALE_PATHS = (
    join(_dir, 'locale'),
)

# Absolute path to the directory that holds static.
# Example: "/home/static/static.lawrence.com/"
MEDIA_ROOT = join(_dir, 'media/')

# URL that handles the static served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = '/media/'

# URL prefix for admin static -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/static/".
ADMIN_MEDIA_PREFIX = '/media/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'ih3^*u=ndnu+nbuv&0)zbd5m2gt%5alzu9*%s!bze2w&r426(6'

STATIC_ROOT = join(_dir, 'static/')
STATIC_URL = '/static/'

#  Folder for static assets that aren’t tied to a particular ap
STATICFILES_DIRS = (
    # Create a static folder at project root if you want
    # os.path.join(SITE_ROOT, 'static'),
)

# List of callables that know how to import templates from various sources.
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            # insert your TEMPLATE_DIRS here
            join(_dir, '..', 'goflow', 'workflow', 'templates'),
            join(_dir, '..', 'goflow', 'apptools', 'templates'),
            join(_dir, '..', 'goflow', 'runtime', 'templates')
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'debug': DEBUG,
            'context_processors': [
                # Insert your TEMPLATE_CONTEXT_PROCESSORS here or use this
                # list if you haven't customized them:
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.media',
                "django.template.context_processors.tz",
                "django.template.context_processors.static",
                "django.template.context_processors.i18n",
            ],
        },
    },
]


MIDDLEWARE = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

ROOT_URLCONF = 'sampleproject.urls'

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.sites',
    'django.contrib.admindocs',
    'django.contrib.staticfiles',
    'goflow.workflow',
    'goflow.graphics',
    'goflow.graphics2',
    'goflow.runtime',
    'goflow.apptools',
    'sampleproject.sampleapp',
    'ninja_simple_jwt',
)

#LOGIN_URL = 'accounts/login'

# mail notification
DEFAULT_FROM_EMAIL = 'sample@project.com'
EMAIL_HOST = 'localhost'

# user that executes auto processes
WF_USER_AUTO = 'auto'
# used to build application url like: http://[web_host]/[WF_APPS_PREFIX]/[application]
WF_APPS_PREFIX = '/sampleapp'
# used to find push functions
WF_PUSH_APPS_PREFIX = 'sampleproject.sampleapp.pushapps'

# test users for fast switch (with DEBUG=TRUE only)
TEST_USERS = (('admin','admin'), ('user1','user1'),
              ('user2','user2'), ('userg1','userg1'))

# the FLAGS_I18N_PREFIX parameter must match urls.py item:
# urls.py     > (r'^PREFIX/i18n/', include('django.conf.urls.i18n')),
# settings.py > FLAGS_I18N_PREFIX = '/PREFIX/i18n/'
FLAGS_I18N_PREFIX = '/lang/i18n/'
# flags served by local server
FLAGS_URL = MEDIA_URL + "flags/"
# flags served by net server
#FLAGS_URL = 'http://djangodev.free.fr/flags/'

# languages
LANGUAGES = (
    ('en', _('English')),
    ('fr', _('French')),
    ('zh-hans', _('Simplified Chinese')),
    ('zh-hant', _('Traditional Chinese')),
    ('ja', _('Japanese')),
    ('ko', _('Korean')),
    ('de', _('German')),
    ('es', _('Spanish')),
    ('it', _('Italian')),
    ('pt', _('Portuguese')),
    ('ru', _('Russian')),
)

NINJA_SIMPLE_JWT = {
    "USE_STATELESS_AUTH": True,
}

# Permissions/roles are managed by the main Django auth system.
GOFLOW_AUTO_CREATE_PROCESS_GROUPS = False
GOFLOW_SCHEDULER_BACKEND = 'goflow.runtime.scheduler.CronSchedulerBackend'
GOFLOW_CONDITION_STRATEGY = 'compatible'
GOFLOW_AUDIT_ENABLED = True
GOFLOW_SLA_ENABLED = True
GOFLOW_SLA_NOTIFY = True
GOFLOW_SLA_AUTO_ASSIGN = False
GOFLOW_WEBHOOK_ENABLED = False
GOFLOW_WEBHOOK_TIMEOUT = 5
GOFLOW_COMPENSATION_AUTO = False

# API access controls (optional)
# Set to None to allow all processes/content types.
GOFLOW_API_ALLOWED_PROCESS_TITLES = ("Sample process", "test parallel workflow")
GOFLOW_API_ALLOWED_CONTENT_TYPES = ("sampleapp.samplemodel",)
GOFLOW_API_REQUIRE_OBJECT_OWNERSHIP = True
GOFLOW_API_OBJECT_OWNER_FIELDS = ("requester",)


