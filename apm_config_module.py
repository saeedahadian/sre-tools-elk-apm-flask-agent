class ApmConfigModule:

    dictConfig = {
        "version": 1,
        "formatters": {
            "simple": {
                "format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
            },
            "elastic": {
                "format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
                + " | elasticapm "
                + "transaction.id=%(elasticapm_transaction_id)s "
                + "trace.id=%(elasticapm_trace_id)s "
                + "span.id=%(elasticapm_span_id)s",
            },
        },
        "handlers": {
            "console": {
                "class": "logging.StreamHandler",
                "formatter": "elastic",
                "level": "INFO",
            },
            "file": {
                "class": "logging.handlers.RotatingFileHandler",
                "formatter": "elastic",
                "level": "INFO",
                "filename": "./apm_agent/trace_logs/app.log",
                "maxBytes": 10 * 1024 * 1024,
                "backupCount": 20,
            },
            "file-error": {
                "class": "logging.handlers.RotatingFileHandler",
                "formatter": "elastic",
                "level": "ERROR",
                "filename": "./apm_agent/trace_logs/app_error.log",
                "maxBytes": 10 * 1024 * 1024,
                "backupCount": 20,
            },
        },
        "root": {
            "level": "DEBUG",
            "handlers": ["console", "file", "file-error"],
        },
        "loggers": {
            "elasticapm": {
                "level": "DEBUG",
                "handlers": ["console"],
                "propagate": True,
            },
        },
    }

    elasticApm = {
        "SERVICE_NAME": "service_name_here",
        "SERVER_URL": "apm_server_address",
        "ENVIRONMENT": "service_environment_here",
        "DEBUG": True,
    }
