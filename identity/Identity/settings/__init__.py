import os


DJANGO_ENV = os.environ.get("DJANGO_ENV", "dev")

if DJANGO_ENV == 'dev':
    from .environments.dev import *


print(f"Selected environment: {DJANGO_ENV}")
