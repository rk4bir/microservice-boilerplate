from ProductAPI.settings.base import *

# Apps list
THIRD_PARTY_APPS = [
    'oauth2_provider',
    'corsheaders',
    'rest_framework'
]
SERVICE_APPS = [
    'products'
]

INSTALLED_APPS += THIRD_PARTY_APPS + SERVICE_APPS
