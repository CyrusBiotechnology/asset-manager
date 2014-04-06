#!/bin/bash


# Local settings location
local_settings="assets/assets/local_settings.py"
local_settings_template="assets/assets/local_settings-template.py"

# Django secret key
secret_key="$(python -c 'import random; print "".join([random.choice("abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)") for i in range(50)])')"
# This files location
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

# setup virtual env
echo 'Setting up virtual environment (env)'
virtualenv --no-site-packages env
pip install -r requirements.txt
echo 'Activating virtual environment'
source env/bin/activate

if [ ! -f  $local_settings ]; then
  cp "$local_settings_template" "$local_settings"
fi
