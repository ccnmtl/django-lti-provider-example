# Django settings for djangoltiproviderexample project.
import os.path
import sys

project = 'djangoltiproviderexample'
base = os.path.dirname(__file__)

DEBUG = True

ADMINS = []
MANAGERS = ADMINS

ALLOWED_HOSTS = [
    'localhost',
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': project,
        'HOST': '',
        'PORT': 5432,
        'USER': '',
        'PASSWORD': '',
        'ATOMIC_REQUESTS': True,
    }
}

if 'test' in sys.argv or 'jenkins' in sys.argv:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': ':memory:',
            'HOST': '',
            'PORT': '',
            'USER': '',
            'PASSWORD': '',
            'ATOMIC_REQUESTS': True,
        }
    }

    PASSWORD_HASHERS = (
        'django.contrib.auth.hashers.MD5PasswordHasher',
    )

JENKINS_TASKS = [
    'django_jenkins.tasks.run_pep8',
    'django_jenkins.tasks.run_pyflakes',
]

TEST_RUNNER = 'django.test.runner.DiscoverRunner'

TIME_ZONE = 'America/New_York'
LANGUAGE_CODE = 'en-us'
SITE_ID = 1
USE_I18N = False
MEDIA_ROOT = "/var/www/" + project + "/uploads/"
MEDIA_URL = '/uploads/'
STATIC_URL = '/media/'
SECRET_KEY = 'you must override this'  # nosec
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(base, "templates"),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                # Insert your TEMPLATE_CONTEXT_PROCESSORS here or use this
                # list if you haven't customized them:
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.debug',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.template.context_processors.request',
                'django.contrib.messages.context_processors.messages'
            ],
        },
    },
]

MIDDLEWARE = [
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
]

AUTHENTICATION_BACKENDS = [
  'django.contrib.auth.backends.ModelBackend',
  'lti_provider.auth.LTIBackend',
]

ROOT_URLCONF = project + '.urls'

INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.flatpages',
    'django.contrib.staticfiles',
    'django.contrib.messages',
    'django.contrib.admin',
    'django_jenkins',
    'lti_provider'
]

INTERNAL_IPS = ['127.0.0.1']

THUMBNAIL_SUBDIR = "thumbs"
EMAIL_SUBJECT_PREFIX = "[" + project + "] "
EMAIL_HOST = 'localhost'
SERVER_EMAIL = project + "@yourdomain"
DEFAULT_FROM_EMAIL = SERVER_EMAIL

STATICMEDIA_MOUNTS = [
    ('/sitemedia', 'sitemedia'),
]

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTOCOL', 'https')
SESSION_ENGINE = "django.contrib.sessions.backends.signed_cookies"
SESSION_COOKIE_HTTPONLY = True
SESSION_COOKIE_SAMESITE = None
SESSION_COOKIE_SECURE = True

STATIC_ROOT = "/tmp/" + project + "/static"  # nosec
STATICFILES_DIRS = ["media/"]
STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder'
]

USE_TZ = True

PROJECT_APPS = [
    'djangoltiproviderexample.main'
]

INSTALLED_APPS += [  # noqa
    'django_bootstrap5',
    'django_extensions',
    'djangoltiproviderexample.main',
]

THUMBNAIL_SUBDIR = "thumbs"
LOGIN_REDIRECT_URL = "/"

ACCOUNT_ACTIVATION_DAYS = 7

LTI_TOOL_CONFIGURATION = {
    'title': 'Sample LTI Tool',
    'description': 'This tool includes launch, navigation and assignments',
    'launch_url': 'lti/',
    'embed_url': '',  # @todo - add an editor embed example
    'embed_icon_url': '',
    'embed_tool_id': '',
    'landing_url': '/',
    'navigation': True,
    'new_tab': True,
    'course_aware': False,
    'frame_width': 1024,
    'frame_height': 1024,
    'assignments': {
        '1': '/assignment/1/',
        '2': '/assignment/2/',
    }
}

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
