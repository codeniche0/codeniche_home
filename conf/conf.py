# Settings file

import os.path

DEBUG = True

PROJECT_PATH = '/'

STATIC_DIR = r'/static/'

EMAIL_USERNAME = ''
EMAIL_PASSWORD = ''
EMAIL_DESTINATION = ''

# This line must go at the end of this file.
try:
    from conf_dev import *
except ImportError:
    pass
