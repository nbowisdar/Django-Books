import logging

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "verbose": {
            "format": "{asctime} {levelname} {filename} {funcName} {lineno} {message}",
            "style": "{",
        },
        "simple": {
            "format": "{asctime} {levelname} - {message}",
            "style": "{",
        },
    },
    "filters": {
        "require_debug_false": {
            "()": "django.utils.log.RequireDebugFalse",
        },
        "require_debug_true": {
            "()": "django.utils.log.RequireDebugTrue",
        },
    },
    "handlers": {
        "console": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "filters": ["require_debug_true"],
            "formatter": "simple",
        },
        "log_file": {
            "level": "DEBUG",
            "class": "logging.handlers.RotatingFileHandler",
            "filename": "api.log",
            "maxBytes": 1024 * 1024 * 5,
            "backupCount": 5,
            "formatter": "verbose",
        },
        "error_file": {
            "level": "ERROR",
            "class": "logging.handlers.RotatingFileHandler",
            "filename": "api_error.log",
            "maxBytes": 1024 * 1024 * 5,
            "backupCount": 5,
            "formatter": "verbose",
        },
        "mail_admins": {
            "level": "ERROR",
            "class": "django.utils.log.AdminEmailHandler",
            "filters": ["require_debug_false"],
            "formatter": "verbose",
        },
    },
    "loggers": {
        "django_project_api": {
            "handlers": ["console", "log_file", "error_file", "mail_admins"],
            "level": "DEBUG",
        },
        "django.request": {
            "handlers": ["mail_admins", "error_file"],
            "level": "ERROR",
            "propagate": False,
        },
    },
}


# Get an instance of a logger
logger = logging.getLogger("django_project_api")


def my_view(request):
    logger.debug("This is a debug message")
    logger.error("This is an error message")
    # Your view logic here
