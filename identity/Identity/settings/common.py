from Identity.settings.base import *

# Apps list
THIRD_PARTY_APPS = [
    'oauth2_provider',
    'corsheaders',
    'rest_framework'
]
SERVICE_APPS = [
    "oauth2",
    "users"
]
INSTALLED_APPS += THIRD_PARTY_APPS + SERVICE_APPS


# Auth config
AUTH_USER_MODEL = 'users.User'
LOGIN_URL = 'users:sign-in'
LOGOUT_URL = 'users:sign-out'
SESSION_COOKIE_AGE = 3600 * 24 * 3


# oauth provider app model
OAUTH2_PROVIDER_APPLICATION_MODEL = 'oauth2.Application'
