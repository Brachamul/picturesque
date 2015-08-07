# -*- coding: utf-8 -*-

"""
Django settings for the project.

"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
	'django.contrib.admin',
	'django.contrib.auth',
	'django.contrib.contenttypes',
	'django.contrib.sessions',
	'django.contrib.messages',
	'django.contrib.staticfiles',
	'medium',
	'PIL',
	'storages' # django-storage-redux
)

MIDDLEWARE_CLASSES = (
	'django.contrib.sessions.middleware.SessionMiddleware',
	'django.middleware.common.CommonMiddleware',
	'django.middleware.csrf.CsrfViewMiddleware',
	'django.contrib.auth.middleware.AuthenticationMiddleware',
	'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
	'django.contrib.messages.middleware.MessageMiddleware',
	'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = '_project.urls'

WSGI_APPLICATION = '_project.wsgi.application'

SITE_NAME = 'Picturesque'

ADMIN_SITE_HEADER = SITE_NAME + ' - Administration'

# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
	'default': {
		'ENGINE': 'django.db.backends.sqlite3',
		'NAME': os.path.join(BASE_DIR, 'project_database.sqlite3'),
	}
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'fr-FR'

TIME_ZONE = 'Europe/Paris'

USE_I18N = True

USE_L10N = True

FIRST_DAY_OF_WEEK = 1 # Lundi, et pas Dimanche comme pour les ricains

# USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'
MEDIA_URL = '/media/'
STATIC_ROOT = os.path.join((BASE_DIR), "_static_root")
MEDIA_ROOT = os.path.join((BASE_DIR), "_media_root")
STATICFILES_DIRS = (
	os.path.join((BASE_DIR), "static", "static"),
)



### CLOUD STORAGE WITH AMAZON S3 !

# https://github.com/jschneier/django-storages

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'

# https://www.caktusgroup.com/blog/2014/11/10/Using-Amazon-S3-to-store-your-Django-sites-static-and-media-files/

AWS_HEADERS = {  # see http://developer.yahoo.com/performance/rules.html#expires
		'Expires': 'Thu, 31 Dec 2099 20:00:00 GMT',
		'Cache-Control': 'max-age=94608000',
	}

AWS_STORAGE_BUCKET_NAME = 'picturesque'
AWS_ACCESS_KEY_ID = 'AKIAJPF2RKAOQO7OY7XQ'
AWS_SECRET_ACCESS_KEY = '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'

# Tell django-storages that when coming up with the URL for an item in S3 storage, keep
# it simple - just use this domain plus the path. (If this isn't set, things get complicated).
# This controls how the `static` template tag from `staticfiles` gets expanded, if you're using it.
# We also use it in the next setting.
AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME

# This is used by the `static` template tag from `static`, if you're using that. Or if anything else
# refers directly to STATIC_URL. So it's safest to always set it.
STATIC_URL = "https://%s/" % AWS_S3_CUSTOM_DOMAIN

# Tell the staticfiles app to use S3Boto storage when writing the collected static files (when
# you run `collectstatic`).
STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'




# Template location

TEMPLATE_DIRS = (
	os.path.join((BASE_DIR), "static", "templates"),
)

from django.contrib import messages
from django.contrib.messages import constants as message_constants

MESSAGE_LEVEL = messages.DEBUG
MESSAGE_TAGS = { messages.ERROR: 'danger' }

#	LOGIN_URL = 'connexion'
#	LOGOUT_URL = 'deconnexion'
#	LOGIN_REDIRECT_URL = 'accueil'



# FRONT-END IMPORTS, using context_processors.py
IMPORT_JQUERY = '<script src="https://ajax.googleapis.com/ajax/libs/jquery/2.1.4/jquery.min.js"></script>'
IMPORT_BOOTSTRAP_JS = '<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/js/bootstrap.min.js"></script>'
IMPORT_BOOTSTRAP_CSS = '<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/css/bootstrap.min.css">'


# MEDIUM SETTING

MEDIUM_SOURCES_URL = 'uploaded/'
MEDIUM_THUMBNAILS_URL = 'thumbnails/'
THUMBNAIL_WIDTH = 1600
THUMBNAIL_HEIGHT = 900

SUCCESSFUL_MEDIA_UPLOAD_MESSAGE = 'Vos photos / vidéos ont bien été chargées.'

##########################
#  Settings localisables :
##########################

# import local_settings if exist
try: from local_settings import *
except ImportError: pass

## Custom, adresse du site utilisée pour envoyer les liens de connexion dans les mails, overridé par local settings
# SITE_URL = "http://localhost:8000"

## Standard, authentification pour l'envoi de mail
# ALLOWED_HOSTS = [SITE_URL,]

## Standard, authentification pour l'envoi de mail
# EMAIL_SUBJECT_PREFIX = "[Élan Démocrate] "
# EMAIL_HOST = "smtp.gmail.com"
# EMAIL_HOST_USER = "patate@gmail.com"
# EMAIL_PORT = 587
# EMAIL_USE_TLS = True
# EMAIL_HOST_PASSWORD = 'azerty12345'

## Standard SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = ''

## Standard SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = False