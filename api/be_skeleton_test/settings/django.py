from pathlib import Path

from .environment import env


BASE_DIR = Path(__file__).resolve().parent.parent


def rel(*path):
    return BASE_DIR.joinpath(*path)


DEBUG = env.bool("BE_SKELETON_TEST_DEBUG", default=False)

INTERNAL_IPS = env.list("BE_SKELETON_TEST_INTERNAL_IPS", default=[])

ALLOWED_HOSTS = env.list("BE_SKELETON_TEST_ALLOWED_HOSTS", default=[])

SECRET_KEY = env.str("BE_SKELETON_TEST_SECRET_KEY")

INSTALLED_APPS = [
    # Django apps
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.sites",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # Third-party apps
    "django_extensions",
    "django_filters",
    "drf_spectacular",
    "rest_framework",
    # First-party apps
    "be_skeleton_test.apps.common",
    "be_skeleton_test.apps.accounts",
] + env.list("BE_SKELETON_TEST_DEV_INSTALLED_APPS", default=[])

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
] + env.list("BE_SKELETON_TEST_DEV_MIDDLEWARE", default=[])

ROOT_URLCONF = "be_skeleton_test.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [rel("templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ]
        },
    }
]

WSGI_APPLICATION = "be_skeleton_test.wsgi.application"

DATABASES = {
    "default": env.db("BE_SKELETON_TEST_DATABASE_URL"),
}

AUTH_USER_MODEL = "accounts.UserAccount"

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

SECURE_CONTENT_TYPE_NOSNIFF = env.bool("BE_SKELETON_TEST_SECURE_CONTENT_TYPE_NOSNIFF", default=True)
SECURE_HSTS_SECONDS = env.int("BE_SKELETON_TEST_SECURE_HSTS_SECONDS", default=31536000)  # 1 year

SESSION_COOKIE_HTTPONLY = env.bool("BE_SKELETON_TEST_SESSION_COOKIE_HTTPONLY", default=True)
SESSION_COOKIE_SECURE = env.bool("BE_SKELETON_TEST_SESSION_COOKIE_SECURE", default=True)
SESSION_COOKIE_NAME = "s"

CSRF_COOKIE_SECURE = env.bool("BE_SKELETON_TEST_CSRF_COOKIE_SECURE", default=True)
CSRF_COOKIE_NAME = "c"

X_FRAME_OPTIONS = env.str("BE_SKELETON_TEST_X_FRAME_OPTIONS", default="SAMEORIGIN")

LANGUAGE_CODE = "en-us"

TIME_ZONE = env.str("BE_SKELETON_TEST_TIME_ZONE", default="UTC")

USE_I18N = True

USE_TZ = True

LOCALE_PATHS = [rel("..", "..", "api", "locale")]


DEFAULT_FILE_STORAGE_BACKEND = env.str(
    "BE_SKELETON_TEST_DEFAULT_FILE_STORAGE_BACKEND", default="storages.backends.s3boto3.S3Boto3Storage"
)
DEFAULT_FILE_STORAGE_OPTIONS = {}
if DEFAULT_FILE_STORAGE_BACKEND == "storages.backends.s3boto3.S3Boto3Storage":
    DEFAULT_FILE_STORAGE_OPTIONS = {
        "bucket_name": env.str("BE_SKELETON_TEST_DEFAULT_FILE_STORAGE_BUCKET_NAME"),
        "endpoint_url": env.str("BE_SKELETON_TEST_DEFAULT_FILE_STORAGE_ENDPOINT_URL"),
        "custom_domain": env.str("BE_SKELETON_TEST_DEFAULT_FILE_STORAGE_CUSTOM_DOMAIN"),
        "url_protocol": env.str("BE_SKELETON_TEST_DEFAULT_FILE_STORAGE_URL_PROTOCOL", default="https:"),
        "location": env.str("BE_SKELETON_TEST_DEFAULT_FILE_STORAGE_LOCATION", default="m"),
        "file_overwrite": env.bool("BE_SKELETON_TEST_DEFAULT_FILE_STORAGE_FILE_OVERWRITE", default=False),
    }

STATICFILES_STORAGE_BACKEND = env.str(
    "BE_SKELETON_TEST_STATICFILES_STORAGE_BACKEND", default="storages.backends.s3boto3.S3StaticStorage"
)
STATICFILES_STORAGE_OPTIONS = {}
if STATICFILES_STORAGE_BACKEND == "storages.backends.s3boto3.S3StaticStorage":
    STATICFILES_STORAGE_OPTIONS = {
        "bucket_name": env.str("BE_SKELETON_TEST_DEFAULT_FILE_STORAGE_BUCKET_NAME"),
        "endpoint_url": env.str("BE_SKELETON_TEST_DEFAULT_FILE_STORAGE_ENDPOINT_URL"),
        "custom_domain": env.str("BE_SKELETON_TEST_DEFAULT_FILE_STORAGE_CUSTOM_DOMAIN"),
        "url_protocol": env.str("BE_SKELETON_TEST_DEFAULT_FILE_STORAGE_URL_PROTOCOL", default="https:"),
        "location": env.str("BE_SKELETON_TEST_STATICFILES_STORAGE_LOCATION", default="s"),
        "file_overwrite": env.bool("BE_SKELETON_TEST_STATICFILES_STORAGE_FILE_OVERWRITE", default=True),
    }


STORAGES = {
    "default": {
        "BACKEND": DEFAULT_FILE_STORAGE_BACKEND,
        "OPTIONS": DEFAULT_FILE_STORAGE_OPTIONS,
    },
    "staticfiles": {
        "BACKEND": STATICFILES_STORAGE_BACKEND,
        "OPTIONS": STATICFILES_STORAGE_OPTIONS,
    },
}

EMAIL_BACKEND = env.str(
    "BE_SKELETON_TEST_EMAIL_BACKEND",
    default="django.core.mail.backends.smtp.EmailBackend",
)

if EMAIL_BACKEND == "django.core.mail.backends.smtp.EmailBackend":  # pragma: no cover
    EMAIL_HOST = env.str("BE_SKELETON_TEST_EMAIL_HOST")
    EMAIL_PORT = env.str("BE_SKELETON_TEST_EMAIL_PORT")
    EMAIL_HOST_USER = env.str("BE_SKELETON_TEST_EMAIL_HOST_USER", default=None)
    EMAIL_HOST_PASSWORD = env.str("BE_SKELETON_TEST_EMAIL_HOST_PASSWORD", default=None)
    EMAIL_USE_TLS = env.bool("BE_SKELETON_TEST_EMAIL_USE_TLS", default=True)

SITE_ID = env.int("BE_SKELETON_TEST_SITE_ID", default=1)

USE_X_FORWARDED_HOST = True

SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

APPEND_SLASH = False

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
