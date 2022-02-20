#!/bin/bash -eux
# In Mac you may have to reinstall python with PYTHON_CONFIGURE_OPTS like below to run this script
# PYTHON_CONFIGURE_OPTS="--enable-framework" pyenv install {python-version}
cd "$( dirname "$0" )"/..
CFLAGS=$(python-config --include) poetry run pyinstaller --onefile --name="switchbot-client-app" --windowed --noconsole switchbot_client_app/main.py
