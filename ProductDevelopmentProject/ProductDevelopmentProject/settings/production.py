from .base import *

SECRET_KEY = os.environ.get("SECRET_KEY")

DEBUG = False

# It ust be defined after deploy is done
ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ.get("POSTGRES_DB", ''),
        'USER': os.environ.get("POSTGRES_USER", ''),
        'PASSWORD': os.environ.get("POSTGRES_PASSWORD", ''),
        'HOST': os.environ.get("POSTGRES_HOST", 'db'),
        'PORT': os.environ.get("POSTGRES_PORT", '5432'),
    }
}

SECURE_CONTENT_TYPE_NOSNIFF = True

SECURE_BROWSER_XSS_FILTER = True

SESSION_COOKIE_SECURE = True

CSRF_COOKIE_SECURE = True

X_FRAME_OPTIONS = 'DENY'
