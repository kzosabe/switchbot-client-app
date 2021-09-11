#!/bin/bash -eux
cd "$( dirname "$0" )"/..
poetry run pyinstaller switchbot_client_app/main.py --onefile --noconsole
