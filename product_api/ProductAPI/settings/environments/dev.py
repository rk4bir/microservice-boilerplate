import os
import sys
import logging.config
from environ import Env
from ..common import *

# Config env file
env = Env()
ENV_FILE = os.path.join(BASE_DIR, '.env.dev')
env.read_env(ENV_FILE)


# secret key
SECRET_KEY = env("SECRET_KEY")


# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'products.dev.sqlite3'),
    }
}


# static and media file config
MEDIA_URL = '/media/'
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]


# oAuth2 provider config
CLIENT_ID = env("CLIENT_ID", default=None)
CLIENT_SECRET = env("CLIENT_SECRET", default=None)
RESOURCE_SERVER_INTROSPECTION_URL = env("RESOURCE_SERVER_INTROSPECTION_URL", default=None)

if not CLIENT_ID or not CLIENT_SECRET or not RESOURCE_SERVER_INTROSPECTION_URL:
    print("CLIENT_ID, CLIENT_SECRET, RESOURCE_SERVER_INTROSPECTION_URL are missing!!!")
    sys.exit(0)

OAUTH2_PROVIDER = {
    'SCOPES': {
        'read': 'Read scope',
        'write': 'Write scope',
        'edit': 'Edit scope',
        'introspection': 'Introspect token scope',
    },
    'RESOURCE_SERVER_INTROSPECTION_URL': RESOURCE_SERVER_INTROSPECTION_URL,
    'RESOURCE_SERVER_INTROSPECTION_CREDENTIALS': (CLIENT_ID, CLIENT_SECRET)
}

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'oauth2_provider.contrib.rest_framework.OAuth2Authentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
    )
}


# Logging config
LOGGING_CONFIG = None
LOGLEVEL = env('DJANGO_LOGLEVEL', default='info').upper()
logging.config.dictConfig({
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'console': {
            'format': '%(asctime)s %(levelname)s [%(name)s:%(lineno)s] %(message)s',
        },
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'console',
        },
    },
    'loggers': {
        '': {
            'level': LOGLEVEL,
            'handlers': ['console'],
        },
    },
})


# Cors config
CORS_ORIGIN_ALLOW_ALL = True
# CORS_ALLOWED_ORIGINS = []
