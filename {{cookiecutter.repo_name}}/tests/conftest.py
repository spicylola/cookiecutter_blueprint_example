import flask_migrate
import pytest
import sqlalchemy
from graphene.test import Client

from {{cookiecutter.repo_name}} import app
from {{cookiecutter.repo_name}} import db
from {{cookiecutter.repo_name}}.schemas.schema import schema

# Retrieve a database connection string from the shell environment
DB_CONN = app.config["SQLALCHEMY_DATABASE_URI"]
DB_TEST = sqlalchemy.engine.url.make_url(DB_CONN).translate_connect_args()

pytest_plugins = ["pytest-flask-sqlalchemy"]


@pytest.fixture(scope="session")
def setup(request):
    """
    Create a Postgres database for the tests, and drop it when the tests are done.
    """
    flask_migrate.upgrade()

    @request.addfinalizer
    def drop_database():
        db.session.close()
        flask_migrate.downgrade(revision="base")


@pytest.fixture(scope="function")
def debug_mode_ctx():
    ctx = app.app_context()
    ctx.app.config["DEBUG"] = True
    ctx.push()
    return ctx


@pytest.fixture(scope="function")
def non_debug_mode_ctx():
    ctx = app.app_context()
    ctx.app.config["DEBUG"] = False
    ctx.push()


@pytest.fixture(scope="session")
def graphql_client():
    ctx = app.app_context()
    ctx.push()
    client = Client(schema)
    return client
