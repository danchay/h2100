
from .base import *

SECRET_KEY = 'qu680xyo799#@7yhebdbchbg%+rcyb+^%hdo*uo(kl=9gt$3z*'

DEBUG = True

DATABASES = {  
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'h2100',                      # Or path to database file if using sqlite3.
        'USER': 'chay',                      # Not used with sqlite3.
        'PASSWORD': 'lopdat',                  # Not used with sqlite3.
        'HOST': 'localhost',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '5432',                      # Set to empty string for default. Not used with sqlite3.
    }
}

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'

# Extra places for collectstatic to find static files.
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')