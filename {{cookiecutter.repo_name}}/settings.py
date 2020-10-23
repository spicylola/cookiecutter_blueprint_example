import os
from distutils.util import strtobool

from utilities import log_helper


class Config:
    HTTP_HOST = os.getenv("HTTP_HOST", "0.0.0.0")
    HTTP_PORT = os.getenv("HTTP_PORT", 5000)

    # NOTE: Set to True to activate the graphql IDE.
    # NOTE: If the ENABLE_IDE envvar is not set we want it to be left
    # as None. The app __init__ will default to the DEBUG value in
    # that case.
    ENABLE_IDE = os.environ.get("ENABLE_IDE", None)
    if ENABLE_IDE is not None:
        ENABLE_IDE = bool(strtobool(os.getenv("ENABLE_IDE")))

    # Database Server and config
    DB_HOST = os.getenv("DB_HOST", "localhost")
    DB_PORT = os.getenv("DB_PORT", "5432")

    DB_DEFAULT_USER = os.getenv("DB_DEFAULT_USER", "postgres")
    DB_DEFAULT_PASS = os.getenv("DB_DEFAULT_PASS")
    DB_DEFAULT_DATABASE = os.getenv("DB_DEFAULT_DATABASE", "postgres")

    DB_USER = os.getenv("DB_USER", "{{cookiecutter.db_username}}")
    DB_PASS = os.getenv("{{cookiecutter.db_password}}")
    DB_DATABASE = os.getenv("DB_DATABASE", "{{cookiecutter.repo_name}}")
    DB_AUTOCREATE = bool(strtobool(os.getenv("DB_AUTOCREATE", "false")))

    SQLALCHEMY_DATABASE_URI = f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_DATABASE}?keepalives_idle=200&keepalives_interval=200&keepalives_count=5"  # noqa: E501
    SQLALCHEMY_ECHO = bool(strtobool(os.getenv("SQLALCHEMY_ECHO", "false")))
    SQLALCHEMY_TRACK_MODIFICATIONS = bool(
        strtobool(os.getenv("SQLALCHEMY_TRACK_MODIFICATIONS", "false"))
    )

    # Logging
    LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
    LOG_SQL = bool(strtobool(os.getenv("LOG_SQL", "false")))

    log_helper.setup_logging(LOG_LEVEL, LOG_SQL)

    # Open Tracing setup
    FEATURE_USE_OPEN_TRACING = bool(strtobool(os.getenv("FEATURE_USE_OPEN_TRACING", "false")))
    JAEGER_HOST = os.getenv("JAEGER_HOST", "jaeger")
    JAEGER_PORT = os.getenv("JAEGER_PORT", "14268")
    JAEGER_SAMPLER = os.getenv("JAEGER_SAMPLER", "const")
    JAEGER_SAMPLER_PARM = os.getenv("JAEGER_SAMPLER_PARM", "1")
    OPEN_TRACING_SERVICE_NAME = "dag-service"

    DOCKER_TAG = os.getenv("DOCKER_TAG", "unknown")