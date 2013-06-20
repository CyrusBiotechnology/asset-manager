#!/bin/bash


# Local settings location
local_settings="assets/assets/local_settings.py"

# Django secret key
secret_key="$(python -c 'import random; print "".join([random.choice("abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)") for i in range(50)])')"
# This files location
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"


# setup virtual env
echo 'Setting up virtual environment (env)'
virtualenv --no-site-packages env
echo 'Activating virtual environment'
source env/bin/activate

# Install requirements
if [ "$(uname)" = "Linux" -a "$(lsb_release -d | awk /buntu/)" != "" ]; then # we only want to do apt-get install on supported systems
  echo 'Installing requirements (May require authentication!)'
  ubuntu_release=$(lsb_release -sr)
  ubuntu_release_int=$(python -c "print '$ubuntu_release'.replace('.', '')")
  sudo apt-get install \
    build-essential \
    python-setuptools \
    python-dev \
    libjpeg62 \
    libjpeg8-dev \
    libfreetype6 \
    libfreetype6-dev \
    zlib1g-dev -qy
  if [ "$ubuntu_release_int" -ge "1009" ]; then
    sudo apt-get install python-pip -qy
    sudo pip install --upgrade pip
  else
    sudo easy_install pip
    sudo pip install --upgrade virtualenv
  fi
fi

sudo pip install --use-mirrors --download-cache ~/.pip-cache/ -r requirements.txt

if [ ! -f  $local_settings ]; then
  echo "

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': '$DIR/assets.db',
    }
}

SECRET_KEY = '$secret_key'

STATIC_ROOT = '$DIR/static/'

STATIC_URL = '/s/'

MEDIA_ROOT = '$DIR/media/'

MEDIA_URL = '/m/'

" > $local_settings
fi

echo 'If there were no errors in setup you may now run ./start.sh to start the server.'
