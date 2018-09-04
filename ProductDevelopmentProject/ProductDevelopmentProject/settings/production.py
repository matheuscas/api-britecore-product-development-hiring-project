from .base import *

SECRET_KEY = os.environ.get("SECRET_KEY")

DEBUG = False

# It ust be defined after deploy is done
ALLOWED_HOSTS = []

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }
