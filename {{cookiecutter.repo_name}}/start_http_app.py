#!/usr/bin/env python
from waitress import serve

import {{cookiecutter.repo_name}}
from config import Config
from utilities import log_helper
from config_service import check_version


def start_server():
    cfg = Config()
    log_helper.log_startup(service_name="{{cookiecutter.repo_name}}",
                           interface_type="http",
                           version=check_version()[-1])
    serve(config_service.get_app(), listen=f"{cfg.HTTP_HOST}:{cfg.HTTP_PORT}")


if __name__ == "__main__":
    start_server()
