# Flask APM Agent

This is a simple setup for APM agent on Flask projects. This directory could be placed inside the service directory or be used as a _submodule_ for the project.

## Introduction

APM uses an agent-server architecture for collecting monitoring data from services. There are available official setups for well-known frameworks like Flask, Spring Boot, etc. This is simply a configuration that could be used for Flask projects. It still requires you to install `elastic-apm` in your project and import this config into your project's source code.

## Usage

You need to install `elastic-apm` in your project before being able to use this configuration. For this purpose, simply add `elastic-apm` to your `requirements.txt` file.

```text
# requirements.txt
elastic-apm[flask]==6.5.0
```

Then, in the main file of your project which is usually named `app.py` or `main.py`, import these packages. Some of these packages might be already imported by your project but add anything that is missing from the list.

```python
# At the top of your main file.
import logging
from elasticapm.contrib.flask import ElasticAPM
from logging.config import dictConfig
from apm_agent.apm_config_module import ApmConfigModule
```

Somewhere after initializing your Flask app, add the following lines to enable your APM.

```python
# First initialize your flask app.
app = Flask(__name__, instance_path=current_dir)

# Enable APM agent.
app.config["ELASTIC_APM"] = ApmConfigModule.elasticApm
dictConfig(ApmConfigModule.dictConfig)
apm = ElasticAPM(app, logging=logging.ERROR)
```

In case you're using `gunicorn` in your production environment and would rather to enable the APM agent only when on production, you can add a cool condition to the above code.

```python
# First initialize your flask app.
app = Flask(__name__, instance_path=current_dir)

# Enable APM agent only if on production.
if "gunicorn" in os.environ.get("SERVER_SOFTWARE", ""):
  app.config["ELASTIC_APM"] = ApmConfigModule.elasticApm
  dictConfig(ApmConfigModule.dictConfig)
  apm = ElasticAPM(app, logging=logging.ERROR)
```

Now, the APM will only be enabled if the service is using `gunicorn` which in many cases is synonymous with being on the production environment.

So far, we added APM to our project's source code. It's time to edit the `apm_config_module.py` file in this repository so that the project can use it correctly. We need to switch some of fields' values with our own at the end of the file.

```python
    elasticApm = {
        "SERVICE_NAME": "service_name_here",
        "SERVER_URL": "apm_server_address",
        "ENVIRONMENT": "service_environment_here",
        "DEBUG": True,
    }
```

Replace `service_name_here`, `apm_server_address`, and `service_environment_here` fields with appropriate values.

Everything is setup and ready to use!
