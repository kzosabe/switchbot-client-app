#!/bin/bash -eu
cd "$( dirname "$0" )"/..
poetry run pytest tests
poetry run black switchbot_client_app tests --check --diff
poetry run isort switchbot_client_app tests --check --diff
poetry run pylint switchbot_client_app tests
poetry run mypy --install-types --non-interactive switchbot_client_app
poetry run mypy switchbot_client_app
