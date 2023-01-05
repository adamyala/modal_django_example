from urllib.parse import urlparse

from .settings import *

DEBUG = False

ALLOWED_HOSTS = [".modal.run"]
CSRF_TRUSTED_ORIGINS = ["https://*.modal.run"]

SECRET_KEY = os.environ["SECRET_KEY"]

database_url = os.environ["DATABASE_URL"]
database_credentials = urlparse(database_url)
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": database_credentials.path.strip("/"),
        "USER": database_credentials.username,
        "PASSWORD": database_credentials.password,
        "HOST": database_credentials.hostname,
        "PORT": "5432",
    }
}
