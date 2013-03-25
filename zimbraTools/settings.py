# -*- coding: utf-8 -*-
# Django settings for zimbraTools project.
import os
from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # (u'Pascal Maurieras', 'pascal.maurieras@nordet.fr'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',  # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'zimbraTools',  # Or path to database file if using sqlite3.
        'USER': 'zimbraTools',  # Not used with sqlite3.
        'PASSWORD': 'uRcvqEwU',  # Not used with sqlite3.
        'HOST': 'localhost',  # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',  # Set to empty string for default. Not used with sqlite3.
    }
}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'Europe/Paris'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'fr-fr'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = '/home/pascal/workspace/zimbraTools/medias/'

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = '/medias/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = ''

PROJECT_ROOT = os.path.dirname(__file__)

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    '/home/pascal/workspace/zimbraTools/static',
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = '4sjqxj5q&amp;-&amp;vvt@mgla_6o9m=fq2!)zkh71ij(4p4889c2j=y_'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

# Template context processors
TEMPLATE_CONTEXT_PROCESSORS = (
                               'django.contrib.auth.context_processors.auth',
                               'django.core.context_processors.debug',
                               'django.core.context_processors.media',
                               'django.core.context_processors.static',
                               'django.core.context_processors.request',
                               'django.core.context_processors.i18n',
                               'django.core.context_processors.csrf',
                               'removeDoublons.context_processors.currentZimbraServer'
                               )

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.RemoteUserMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'zimbraTools.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'zimbraTools.wsgi.application'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    '/home/pascal/workspace/zimbraTools/templates'
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Uncomment the next line to enable the admin:
    'django.contrib.admin',
    # Uncomment the next line to enable admin documentation:
    'django.contrib.admindocs',
    'removeDoublons',
    'django_ldapbackend',
    'south',
)

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

AUTHENTICATION_BACKENDS = (
    # 'django_auth_ldap.backend.LDAPBackend',
    'django.contrib.auth.backends.ModelBackend',
    'django.contrib.auth.backends.RemoteUserBackend',
)

# AUTH_LDAP_SERVER_URI = "ldap://mail.nordet.org"
# Required
AUTH_LDAP_SERVER = "ldap://mail.nordet.org:390"  # Hostname
AUTH_LDAP_BASE_USER = "uid=zimbra,cn=admins,cn=zimbra"  # Administrative User's Username
AUTH_LDAP_BASE_PASS = "KvgU47sWM"  # Administrative User's Password 
AUTH_LDAP_BASE_DN = "dc=nordet,dc=org"  # Base DN (also accepts o=example.com format)
AUTH_LDAP_FIELD_DOMAIN = "nordet.org"  # Domain from which users will take the domain for dummy e-mail generation (it keeps Django happy!)
AUTH_LDAP_GROUP_NAME = "ldap_people"  # Django group for LDAP users (helps us manage them for password changing, etc.)
AUTH_LDAP_VERSION = 3  # LDAP version
AUTH_LDAP_OLDPW = False  # Can the server take the old password? True/False

# Optional
AUTH_LDAP_FIELD_USERAUTH = "uid"  # The field from which the user authentication shall be done.
AUTH_LDAP_FIELD_AUTHUNIT = "people"  # The organisational unit in which your users shall be found.
AUTH_LDAP_FIELD_USERNAME = "uid"  # The field from which to draw the username (Default 'uid'). (Allows non-uid/non-dn custom fields to be used for login.)
AUTH_LDAP_WITHDRAW_EMAIL = False  # Should django try the directory for the user's email ('mail')? True/False.

LOGIN_URL = '/login'  # Lien vers la page si l'authentification échoue
LOGIN_REDIRECT_URL = '/dashboard'  # Lien vers la page si l'authentification réussi

#
# Constantes pour appli clearZimbra
# ZIMBRA_SERVER = 'mail.nordet.org'
