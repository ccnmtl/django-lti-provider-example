# flake8: noqa
from djangoltiproviderexample.settings_shared import *

try:
    from djangoltiproviderexample.local_settings import *
except ImportError:
    pass
