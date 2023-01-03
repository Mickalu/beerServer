from .base import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'beers',
        'USER': 'postgres',
        'PASSWORD': '',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}
CORS_ALLOW_CREDENTIALS = True

CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
]

CORS_ALLOW_HEADERS = [
    "access-control-allow-origin",
    "*",
]

CORS_ALLOW_METHODS = ["GET", "POST", "PUT"]

ALLOWED_HOSTS = []

DEBUG = True
