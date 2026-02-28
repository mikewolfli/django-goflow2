# Django settings for openflow project.
import os
import sys
from os.path import dirname, join
from django.utils.translation import gettext_lazy as _

_dir = dirname(__file__)

LIB_PATH = join(_dir,'..')

SITE_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#SITE_ROOT = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
sys.path.append(LIB_PATH)

DEBUG = True
# TEMPLATE_DEBUG = DEBUG

LOGIN_URL = 'accounts/login/'

ADMINS = (
    # ('Your Name', 'your_email@domain.com'),
)

MANAGERS = ADMINS

#old configs
# DATABASE_ENGINE = 'sqlite3'           # 'postgresql', 'mysql', 'sqlite3' or 'ado_mssql'.
# DATABASE_NAME = join(_dir, 'sqlite.db3')             # Or path to database file if using sqlite3.
# DATABASE_USER = ''             # Not used with sqlite3.
# DATABASE_PASSWORD = ''         # Not used with sqlite3.
# DATABASE_HOST = ''             # Set to empty string for localhost. Not used with sqlite3.
# DATABASE_PORT = ''             # Set to empty string for default. Not used with sqlite3.

'''

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
        'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        # 'NAME': os.path.join(SITE_ROOT, 'Database') + '/WBDAP.db', # Or path to database file if using sqlite3.
        'NAME': os.path.join(_dir) + '/sqlite.db3', # Or path to database file if using sqlite3.
        'USER': '', # Not used with sqlite3.
        'PASSWORD': '', # Not used with sqlite3.
        'HOST': '', # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '', # Set to empty string for default. Not used with sqlite3.
    },
}
'''
if os.environ.get('GOFLOW_USE_PG', '').lower() in ('1', 'true', 'yes'):
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': os.environ.get('GOFLOW_PG_DB', 'leavedemo'),
            'USER': os.environ.get('GOFLOW_PG_USER', 'postgres'),
            'PASSWORD': os.environ.get('GOFLOW_PG_PASSWORD', ''),
            'HOST': os.environ.get('GOFLOW_PG_HOST', '127.0.0.1'),
            'PORT': os.environ.get('GOFLOW_PG_PORT', '5432'),
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(_dir, 'sqlite.db3'),
        }
    }



# Local time zone for this installation. All choices can be found here:
# http://www.postgresql.org/docs/current/static/datetime-keywords.html#DATETIME-TIMEZONE-SET-TABLE
TIME_ZONE = 'Asia/Shanghai'

# Language code for this installation. All choices can be found here:
# http://www.w3.org/TR/REC-html40/struct/dirlang.html#langcodes
# http://blogs.law.harvard.edu/tech/stories/storyReader$15
LANGUAGE_CODE = 'zh-hans'

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

LOCALE_PATHS = (
    join(_dir, 'locale'),
)

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True
DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'

# Absolute path to the directory that holds user uploaded files.
# Example: "/home/static/static.lawrence.com/"
MEDIA_ROOT = join(_dir, 'media/')

# URL that handles the static served from MEDIA_ROOT.
# Example: "http://media.lawrence.com"
MEDIA_URL = '/files/'

# URL prefix for admin static -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/static/".
# ADMIN_MEDIA_PREFIX = '/static/'
STATIC_URL = '/static/'
STATIC_ROOT = ''

STATICFILES_DIRS = (join(_dir, 'static'),)
# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)



# Make this unique, and don't share it with anybody.
SECRET_KEY = '%@48o#l@iz!ybjl_2_1smc#%*u+^m0m^18ghw-6=3k48g2rt8^'

# List of callables that know how to import templates from various sources.
# TEMPLATE_LOADERS = (
#     'django.template.loaders.filesystem.load_template_source',
#     'django.template.loaders.app_directories.load_template_source',
# #     'django.template.loaders.eggs.load_template_source',
# )



TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            # insert your TEMPLATE_DIRS here
            join(_dir, 'templates').replace('\\', '/'), 
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



MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    # 'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'leavedemo.urls'
#
# TEMPLATE_DIRS = (
#     join(_dir,'..', 'goflow', 'apptools', 'templates'),
#     join(_dir,'..', 'goflow', 'runtime', 'templates')
# )

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.messages',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.admin',
    'django.contrib.staticfiles',
    'goflow.workflow',
    'goflow.graphics',
    'goflow.graphics2',
    'goflow.runtime',
    'goflow.apptools',
    'leavedemo.leave',
    'ninja_simple_jwt',
)

#username and password
TEST_USERS = (
            ('primus','p'),('notarius','n'),('prefectus','p'),
            ('socius','s'),('secundus','s'),('tertius','t'),('quartus','q')
)
WF_USER_AUTO = 'auto'
WF_APPS_PREFIX = '/leave'
WF_PUSH_APPS_PREFIX = 'leavedemo.leave.pushapplications'

# mail notification settings
DEFAULT_FROM_EMAIL = 'goflow <goflow@alwaysdata.net>'
EMAIL_HOST = 'smtp.alwaysdata.com'
EMAIL_SUBJECT_PREFIX = '[Goflow notification]'

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
GOFLOW_API_ALLOWED_PROCESS_TITLES = ("leave", "Gestion des absences")
GOFLOW_API_ALLOWED_CONTENT_TYPES = ("leave.leaverequest",)
GOFLOW_API_REQUIRE_OBJECT_OWNERSHIP = True
GOFLOW_API_OBJECT_OWNER_FIELDS = ("requester",)
