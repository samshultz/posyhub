"""
Django settings for posyhubcomng project.

Generated by 'django-admin startproject' using Django 1.11.16.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(os.path.join(__file__, os.pardir))))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '_-319@k33+)(lbd8v58(yo1x!5zt4w7a_&xo=v-6mr_$vm*qa('

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'constance',
    'constance.backends.database',
    'suit',
    'django.contrib.admin',
    'django.contrib.sites',
    'django.contrib.sitemaps',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    # my apps
    'contact',
    'about',
    'services',
    'snippets',

    # third party apps
    
    'sorl.thumbnail',
    'fluent_comments',
    'crispy_forms',
    'threadedcomments',
    'django_comments',
    'mptt',
    'tagging',
    'zinnia',
    'ckeditor',
    'ckeditor_uploader',
    'zinnia_ckeditor',
    'addendum',
    'widget_tweaks',
    'robots',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'posyhubcomng.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        # 'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'posyhubcomng.context_processors.active_menu',
                'constance.context_processors.config',
            ],
            'loaders': [
                'app_namespace.Loader',
                'django.template.loaders.filesystem.Loader',
                'django.template.loaders.app_directories.Loader',
            ],
        },
    },
]

WSGI_APPLICATION = 'posyhubcomng.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static/')


SITE_ID = 1

# CKEDITOR CONFIGS
CKEDITOR_UPLOAD_PATH = "uploads/"
CKEDITOR_IMAGE_BACKEND = "pillow"

CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'full',
        'skin': 'moono',
        'extraPlugins': 'toc',
    },

    'basic': {
        'skin': 'moono',
        'toolbar': 'Custom',
        'toolbar_Basic': [
            ['Source', '-', 'Bold', 'Italic']
        ],
        'toolbar_Custom': [
            {'name': 'editing', 'items': ['Find', 'Replace', '-', 'SelectAll']},
            {'name': 'paragraph',
             'items': ['NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', '-', '-',
                       'JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock', '-']},
            {'name': 'links', 'items': ['Link', 'Unlink', 'Anchor']},
            {'name': 'insert', 'items': ['Image']}, 
            {'name': 'styles', 'items': ['Styles', 'Format', 'Font', 'FontSize']},
        ]
    }
}

# DJANGO CONSTANCE CONFIG

CONSTANCE_ADDITIONAL_FIELDS = {
    'url_field': ['django.forms.URLField', {}]
}
CONSTANCE_CONFIG = {
    'Facebook': ('', 'The URL to your facebook page', 'url_field'),
    'Twitter': ('', 'The URL of your twitter page', 'url_field'),
    'LinkedIn': ('', 'The URL of your LinkedIn page', 'url_field'),
    'Google+': ('', 'The URL of your Google plus page', 'url_field'),
    'OPENING_HOURS': ('8AM', 'The time your office opens for work everyday'),
    'CLOSING_HOURS': ('6PM', 'The time your office closes from work everyday')
}

CONSTANCE_CONFIG_FIELDSETS = {
    'Social Media Settings': ('Facebook', 'Twitter', 'LinkedIn', 'Google+'),
    'Timing': ('OPENING_HOURS', 'CLOSING_HOURS'),
}
CONSTANCE_BACKEND = 'constance.backends.database.DatabaseBackend'
CONSTANCE_IGNORE_ADMIN_VERSION_CHECK = True

# ZINNIA SETTINGS
ZINNIA_PAGINATION = 6

# COMMENTS XTD SETTINGS
COMMENTS_APP = 'fluent_comments'
CRISPY_TEMPLATE_PACK = 'bootstrap3'

# DJANGO ROBOTS SETTINGS
ROBOTS_USE_SCHEME_IN_HOST = True

# DJANGO SUIT CONFIG
SUIT_CONFIG = {
    "ADMIN_NAME": "Posyhub Admin",
    'MENU_ICONS': {
        'tagging': 'icon-tags',
        'sites': 'icon-leaf',
        'auth': 'icon-lock',
        'services': 'icon-screenshot',
        'about': 'icon-book',
        'contact': 'icon-bookmark',
        'constance': 'icon-cog',
        'zinnia': 'icon-th',
        'threadedcomments': 'icon-comment',
        'django_comments': 'icon-comment',
        'addendum': 'icon-pencil',
        'robots': 'icon-fire'
    },
}