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
                'NAME': '/path/to/database/file.db'
            }
        }

        SECRET_KEY = ''  # https://docs.djangoproject.com/en/dev/ref/settings/#s-secret-key

        STATIC_URL = '/s/'

        MEDIA_ROOT = '/path/to/a/directory/'  # this must be writeable


*   enter the python virtual enviornment:

        source ./env/bin/activate


*   sync the database:
        
        ./assets/manage.py syncdb

[follow prompts]


*   run a server:

        ./assets/manage.py runserver 2000  


*   view the application:

        http://localhost:2000/