from .base import *
import django_heroku

DEBUG = False

ALLOWED_HOSTS = ["posyhub.pythonanywhere.com","www.posyhub.com", "posyhub.com", "posyhub.com.ng", "www.posyhub.com.ng", "*.posyhub.com.ng"]


ADMINS = (
    ('Samuel Taiwo', 'taiwogabrielsamuel@gmail.com'),
    ('Lucky Pius', 'luckypius5@gmail.com')
)

SECRET_KEY = os.environ.get("SECRET_KEY", "+)(&%$Ytfhgfvugyu5rre6643rtyg)(*&6545/5*&W#$!@&&a7-i7_-319@k33+)(lb!_*^(*&()*)*fdvsappmy0$f(v3any06v&1cw4c!gh%1x)@")

# DATABASES
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'HOST': "posyhub.mysql.pythonanywhere-services.com",
        'NAME': 'posyhub$posyhubcomng',
        'USER': 'posyhub',
        'PASSWORD': 'reductionismposyhubcomng',
    }
}


# DJANGO STORAGES SETTINGS
DEFAULT_FILE_STORAGE = 'storages.backends.gcloud.GoogleCloudStorage'
GS_BUCKET_NAME = 'posyhub_media'

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

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')