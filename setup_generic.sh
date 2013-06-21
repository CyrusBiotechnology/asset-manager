#!/bin/bash


# Local settings location
local_settings="assets/assets/local_settings.py"
local_settings_template="assets/assets/local_settings-template.py"

# Django secret key
secret_key="$(python -c 'import random; print "".join([random.choice("abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)") for i in range(50)])')"
# This files location
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

# Install prerequisites
    sudo apt-get install \
      build-essential \
      python-setuptools \
      python-dev \
      libjpeg62 \
      libjpeg8-dev \
      libfreetype6 \
      libfreetype6-dev \
      zlib1g-dev -qy
      sudo apt-get install python-pip -qy
      sudo pip install --upgrade pip

# setup virtual env
echo 'Setting up virtual environment (env)'
virtualenv --no-site-packages env
echo 'Activating virtual environment'
source env/bin/activate
sudo pip install --use-mirrors --download-cache ~/.pip-cache/ -r requirements.txt

if [ ! -f  $local_settings ]; then
  cp "$local_settings_template" "$local_settings"
fi

echo 'If there were no errors in setup you may now run ./start.sh to start the server.'
