#!/bin/bash -eu
poetry run pyinstaller --name="switchbot-client-app" --windowed switchbot_client_app/main.py
