from .base import *

logger.warning("Production settings is active...")

ALLOWED_HOSTS = eval(os.environ.get("ALLOWED_HOSTS"))

DEBUG = False

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": os.environ.get("DATABASES_NAME"),
        "USER": os.environ.get("DATABASES_USER"),
        "PASSWORD": os.environ.get("DATABASES_PASSWORD"),
        "HOST": os.environ.get("DATABASES_HOST"),
        "PORT": os.environ.get("DATABASES_PORT"),
    }
}

DATABASES['default']['ATOMIC_REQUESTS'] = True
