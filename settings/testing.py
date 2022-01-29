from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

INSTALLED_APPS = INSTALLED_APPS + [
    # "django_extensions",
    # "debug_toolbar",
]

# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = "django-insecure-o@@qo2825xscg)1^uur63n_t#$7z-#2o9ps&lyx@+4#lptkivy"

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ["*"]


INTERNAL_IPS = [
    # ...
    "127.0.0.1",
    "localhost",
    # ...
]

# EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"


try:
    from .local import *
except ImportError:
    pass


# uncomment this to whack logging up to maximum
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {"console": {"class": "logging.StreamHandler",},},
    "django": {"handlers": ["console"], "level": "DEBUG",},
}
