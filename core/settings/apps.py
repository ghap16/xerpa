# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # THIRD_PARTY
    "rest_framework",
    "drf_yasg",
    # MY APPS
    "common",
    "transactions",
    "transaction_enrichment",
]
