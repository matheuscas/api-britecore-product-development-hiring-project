from .base import *

SECRET_KEY = os.environ.get("SECRET_KEY")

DEBUG = False

# It ust be defined after deploy is done
ALLOWED_HOSTS = ["6aer4573jb.execute-api.us-west-2.amazonaws.com"]

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

INSTALLED_APPS += [
    "storages"
]

AWS_STORAGE_BUCKET_NAME = 'zappa-britecore-s3-static'

AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME

STATIC_URL = "https://%s/" % AWS_S3_CUSTOM_DOMAIN

STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'

SECURE_CONTENT_TYPE_NOSNIFF = True

SECURE_BROWSER_XSS_FILTER = True

# SESSION_COOKIE_SECURE = True

# CSRF_COOKIE_SECURE = True

X_FRAME_OPTIONS = 'DENY'
