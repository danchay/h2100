from .base import *

DEBUG = False
SECRET_KEY=os.environ['SECRET_KEY']





ALLOWED_HOSTS = ['hackingto100.com', 'www.hackingto100.com', 'h2100.herokuapp.com']


ROOT_URLCONF = 'h2100.urls'
ROOT_HOSTCONF = 'h2100.hosts'
DEFAULT_HOST = 'www'
DEFAULT_REDIRECT_URL = "http://www.hackingto100.com"
PARENT_HOST = "hackingto100.com"

WSGI_APPLICATION = 'h2100.wsgi.application'


# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'h2100.db'),
#     }
# }

# Update database configuration with $DATABASE_URL. This is for Heroku.
import dj_database_url
db_from_env = dj_database_url.config()
DATABASES['default'].update(db_from_env)


# Extra places for collectstatic to find static files.
STATICFILES_DIRS = (
    os.path.join(PROJECT_ROOT, 'static'),
)
STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'


AWS_QUERYSTRING_AUTH = False
AWS_ACCESS_KEY_ID = os.environ['AWS_ACCESS_KEY_ID']
AWS_SECRET_ACCESS_KEY = os.environ['AWS_SECRET_ACCESS_KEY']
AWS_STORAGE_BUCKET_NAME = os.environ['S3_BUCKET_NAME']
MEDIA_URL = 'http://%s.s3.amazonaws.com/media/' % AWS_STORAGE_BUCKET_NAME
DEFAULT_FILE_STORAGE='storages.backends.s3boto3.S3Boto3Storage'

