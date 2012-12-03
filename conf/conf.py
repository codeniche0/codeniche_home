# Settings file

import os.path

DEBUG = True

PROJECT_PATH = '/'

STATIC_DIR = r'/static/'

EMAIL_USERNAME = ''
EMAIL_PASSWORD = ''
EMAIL_DESTINATION = ''

# This line must go at the end of this file.
if os.path.exists('conf_dev.py'):
    from conf_dev import *
