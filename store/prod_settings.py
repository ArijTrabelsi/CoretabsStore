import os

import dj_database_url

from .settings import *

SECRET_KEY = os.environ.get('SECRET_KEY')

DEBUG = False

ALLOWED_HOSTS = ['afternoon-everglades-55160.herokuapp.com']

DATABASE_URL = {
    'default': dj_database_url.config(default=os.environ.get('DATABASE_URL'))
} 