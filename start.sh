#!/bin/bash
echo 'If this is your first time running the server setup.sh MUST be run first!'

echo 'Activating the environment ...'
source env/bin/activate

echo 'Syncing the database ...'
./assets/manage.py syncdb --migrate

echo 'Running the server ...'
./assets/manage.py runserver 2000
