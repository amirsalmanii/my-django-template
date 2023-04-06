from .base import *

logger.warning("Local settings is active...")

ALLOWED_HOSTS = ["*"]

DEBUG = True

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": '{{cookiecutter.project_slug}}',
        "USER": '{{cookiecutter.postgres_user}}',
        "PASSWORD": '{{cookiecutter.postgres_password}}',
        "HOST": os.environ.get("DATABASES_HOST", "127.0.0.1"),
        "PORT": os.environ.get("DATABASES_PORT", 5432),
    }
}

DATABASES['default']['ATOMIC_REQUESTS'] = True

from config.confd.swagger import * # noqa

CORS_ALLOW_CREDENTIALS = True
CORS_ALLOW_ALL_ORIGINS = True