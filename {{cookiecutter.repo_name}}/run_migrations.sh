#!/usr/bin/env bash
#
echo "Running migrations..."
export FLASK_APP=functions_service/__init__.py
flask db upgrade
