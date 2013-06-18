import os

# Full filesystem path to the project.
PROJECT_ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../')

DATABASES = {
        'default': {
                  'ENGINE': 'django.db.backends.sqlite3',
                          'NAME': '/var/db/pnovotnak/assets.db'
                              }
        }

SECRET_KEY = '43$6mf@^6nj-@e4slkmef309qu5y09bmpo59456u309384)(*&)(*&=++'

STATIC_ROOT = os.path.join(PROJECT_ROOT, 'static/')

STATIC_URL = '/s/'

MEDIA_ROOT = os.path.join(PROJECT_ROOT, 'media/')

MEDIA_URL = '/m/'

