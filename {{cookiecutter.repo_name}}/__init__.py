import logging
import os
import time

from flask import Flask
from flask_cors import CORS
from flask_graphql import GraphQLView
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from healthcheck import EnvironmentDump  # noqa: F401
from healthcheck import HealthCheck
from utilities.graphql_opentracing import build_traced_graphql

from {{cookiecutter.repo_name}} import settings
from utilities import log_helper

os.environ["TZ"] = "UTC"
time.tzset()


app = Flask(__name__)
app.config.from_object(settings.Config)

db = SQLAlchemy(app)
migrate = Migrate(app, db)
CORS(app)
logger = logging.getLogger()


# NOTE: These Imports need to be here after migrate is instantiated so
# that alembic will be able to pickup our modles for automigration.
from {{cookiecutter.repo_name}} import models  # noqa: 402
from {{cookiecutter.repo_name}}.schemas.schema import schema  # noqa: #402


def get_graphiql_flag():
    graphiql_flag = False
    if app.config["ENABLE_IDE"] is None:
        # NOTE: If ENABLE_IDE is not set, fallback to DEBUG
        if app.debug:
            graphiql_flag = True
    else:
        if app.config["ENABLE_IDE"]:
            graphiql_flag = True
    return graphiql_flag


# Register the health check
health = HealthCheck(app, "/healthcheck")


def check_version():
    build_version = settings.Config.DOCKER_TAG
    return True, f"{build_version}"


health.add_check(check_version)

# This code is disabled until a more reliable solution can be
# developed.  Feel free to use locally or on feature branches, but it
# can't go to /develop.
# if app.config['DEBUG']:
#    EnvironmentDump(app, "/environment")


def get_app():
    return build_traced_graphql(app, schema, get_graphiql_flag(), settings)


@app.cli.command("test_func")
def test_func():
    print("Ran test func")