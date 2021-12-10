#!/bin/bash -eu
cd "$( dirname "$0" )"/..
poetry run isort switchbot_client_app tests
poetry run black switchbot_client_app tests
