# flake8: noqa
from djangoltiproviderexample.settings_shared import *
from ccnmtlsettings.compose import common

locals().update(
    common(
        project=project,
        base=base,
        STATIC_ROOT=STATIC_ROOT,
        INSTALLED_APPS=INSTALLED_APPS,
    ))

try:
    from djangoltiproviderexample.local_settings import *
except ImportError:
    pass
