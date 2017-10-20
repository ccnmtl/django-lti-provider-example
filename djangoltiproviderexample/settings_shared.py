# Django settings for djangoltiproviderexample project.
import os.path
from ccnmtlsettings.shared import common

project = 'djangoltiproviderexample'
base = os.path.dirname(__file__)

locals().update(common(project=project, base=base))

PROJECT_APPS = [
    'djangoltiproviderexample.main',
]

USE_TZ = True

MIDDLEWARE_CLASSES += [  # noqa
    'wagtail.wagtailcore.middleware.SiteMiddleware',
    'wagtail.wagtailredirects.middleware.RedirectMiddleware',
]

INSTALLED_APPS += [  # noqa
    'bootstrap3',
    'infranil',
    'django_extensions',
    'djangoltiproviderexample.main',
]

THUMBNAIL_SUBDIR = "thumbs"
LOGIN_REDIRECT_URL = "/"

ACCOUNT_ACTIVATION_DAYS = 7
