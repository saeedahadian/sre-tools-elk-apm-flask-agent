# Flask APM Agent

This is a simple APM and log configuration for flask applications. This
file should be put aside other project files in _the root_ of the
project. The resulting logs are created inside the `logs` directory in
the root of the project.

## PreSetup
You might need to source your `venv` before-hand and use this command

`python3 -m  venv  venv`

`source source venv/bin/activate`



## Setup

‌To setup flask for using this configuration, follow these steps:

1. Install Elastic APM agent using pip:

```bash
pip install elastic-apm[flask]
```
to update your `requirements.txt`.
```bash
pip freeze > requirements.txt
```



2. Import these modules in your app's main file:

```python
import logging
from elasticapm.contrib.flask import ElasticAPM
from logging.config import dictConfig
from apmconfigmodule import ApmConfigModule
```

3. you need to add these couple of lines in the main script of the 
application, somewhere between the `app` and the `apm` declarations.

```python
app = Flask(__name__) # app declaration

# These 2 lines are used to read APM configurations.
app.config["ELASTIC_APM"] = ApmConfigModule.elasticApm;
dictConfig(ApmConfigModule.dictConfig)

apm = ElasticAPM(app, logging=logging.ERROR)  # apm declaration
```

4. Change the values of `SERVICE_NAME` and `ENVIRONMENT` to your
service's appropriate values inside `apmconfigmodule.py`.

```python
elasticApm = {
     "SERVICE_NAME": "qa_api",
     "SERVER_URL": "http://ai-monitoring.emofid.com:9204",
     "ENVIRONMENT": "development",
     "DEBUG": True,
}
```

5. Now use `app.logger.<level>` to add logs in your project.

