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
                "filename": "./logs/app.log",
                "maxBytes": 10 * 1024 * 1024,
                "backupCount": 20,
            },
            "file-error": {
                "class": "logging.handlers.RotatingFileHandler",
                "formatter": "elastic",
                "level": "ERROR",
                "filename": "./logs/app-error.log",
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

    @staticmethod
    def elasticApm(config):
        return {
            "SERVICE_NAME": config["SERVICE_NAME"],
            "SERVER_URL": "http://10.1.19.1:9204",
            "ENVIRONMENT": config["ENVIRONMENT"],
            "DEBUG": True,
        }
