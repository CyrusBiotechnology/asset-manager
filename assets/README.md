Asset Manager
=============

..is an asset manager that is generic enough that it should be able to handle most asset tracking needs.





Getting Started
---------------

*    check out the repository and run:

        $ setup.sh

*    create an assets/assets/local_settings.py file, you'll need to define three parameters here:
        

        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': '/var/db/pnovotnak/assets.db'
            }
        }

        SECRET_KEY = ''  # https://docs.djangoproject.com/en/dev/ref/settings/#s-secret-key

        STATIC_URL = '/s/'

        MEDIA_ROOT = '/Users/pnovotnak/Documents/asset-manager/assets/media/'


