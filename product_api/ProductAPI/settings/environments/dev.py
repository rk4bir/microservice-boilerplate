import os
import logging.config

from ..common import *


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
client_id = 'qEQ6ZmJHkDFOlPRmH2JxL0jcKLniU8Bb1Pfi0ccz'
client_secret = 'BgvFEHQqkMhhLqpZAN7f294L4DtlagqzyGMNxQiS6EskzxMpLVJhxGg7DEHzAyLHPY32EHypdgwvOwDuvEisLaDTnFF9XMAOAbMsgOyQp4J9VcroRapEyQDqz4tU1R0V'
OAUTH2_PROVIDER = {
    'SCOPES': {
        'read': 'Read scope',
        'write': 'Write scope',
        'edit': 'Edit scope',
        'introspection': 'Introspect token scope',
    },
    'RESOURCE_SERVER_INTROSPECTION_URL': 'http://127.0.0.1:8000/oauth2/introspect/',
    'RESOURCE_SERVER_INTROSPECTION_CREDENTIALS': (client_id, client_secret)
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
LOGLEVEL = os.getenv('DJANGO_LOGLEVEL', 'info').upper()
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
