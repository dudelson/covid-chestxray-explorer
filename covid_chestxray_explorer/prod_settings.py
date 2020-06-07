import os
from .default_settings import *

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ['DJANGO_SECRET_KEY']

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = [os.environ['DJANGO_PROD_HOST']]

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

# TODO: change to postgres
DATABASES = {
}

# static files
# TODO are these settings actually necessary for my app? (I suspect not.)
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'
