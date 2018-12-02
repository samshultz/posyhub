from .base import *
import django_heroku 

DEBUG = True

ALLOWED_HOSTS = ["posyhub.herokuapp.com","www.posyhub.com", "posyhub.com", "posyhub.com.ng", "www.posyhub.com.ng", "*.posyhub.com.ng"]


ADMINS = (
    ('Samuel Taiwo', 'taiwogabrielsamuel@gmail.com'),
    ('Lucky Pius', 'luckypius5@gmail.com')
)

SECRET_KEY = os.environ.get("SECRET_KEY", "*pgdt3h3ta7-i7_-319@k33+)(lb!_*^(*&()*)*fdvsappmy0$f(v3any06v&1cw4c!gh%1x)@")

# DATABASES
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'HOST': "ec2-184-72-239-186.compute-1.amazonaws.com",
        'NAME': 'd4iu7m19mdqoni',
        'USER': 'gomuglrevsbqmd',
        'PASSWORD': os.environ.get("DATABASE_PWD"),
    }
}

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = os.environ.get("EMAIL")
EMAIL_HOST_PASSWORD = os.environ.get("EMAIL_PWD")
EMAIL_PORT = 587
EMAIL_USE_TLS = True

SECURE_SSL_REDIRECT = True
CSRF_COOKIE_SECURE = True

# DJANGO STORAGES SETTINGS
DEFAULT_FILE_STORAGE = 'storages.backends.gcloud.GoogleCloudStorage'
GS_BUCKET_NAME = 'POSYHUB_MEDIA'

from google.oauth2 import service_account

GS_CREDENTIALS = service_account.Credentials.from_service_account_file(
    os.path.join(BASE_DIR, 'analytics.json')
)
GS_AUTO_CREATE_BUCKET = True

# Security Settings
CORS_REPLACE_HTTPS_REFERER = True
HOST_SCHEME = "https://"
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_BROWSER_XSS_FILTER = True

SECURE_HSTS_SECONDS = 1000000
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True

SECURE_FRAME_DENY = True
X_FRAME_OPTIONS = "DENY"
django_heroku.settings(locals())

RQ_QUEUES = {
    'default': {
        'HOST': 'localhost',
        'PORT': 6379,
        'DB': 0,
        'DEFAULT_TIMEOUT': 360,
    },

    'high': {
        'URL': os.getenv('REDISTOGO_URL', 'redis://localhost:6379/0'),
        'DEFAULT_TIMEOUT': 500,
    },
    'low': {
        'HOST': 'localhost',
        'PORT': 6379,
        'DB': 0,
    },
}

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')