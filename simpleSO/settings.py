"""
Django settings for simpleSO project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

SITE_ID = 1


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '!wwr=0jwe_&1f$dd6q$p^!%694n%)u^zyb0(v&!amz&j0+j394'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = ['localhost', '127.0.0.1', ]

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.sites',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'registration',
    'bootstrap3',
    'social_auth',
)

# Email server setings

ACCOUNT_ACTIVATION_DAYS = 1
REGISTRATION_AUTO_LOGIN = True
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = True
EMAIL_HOST = "smtp.gmail.com"
EMAIL_HOST_USER = "emptinessssssssss@gmail.com"
DEFAULT_FROM_EMAIL = "emptinessssssssss@gmail.com"
SERVER_EMAIL = "emptinessssssssss@gmail.com"
EMAIL_HOST_PASSWORD = "qz1awx2s"
EMAIL_PORT = 587

# Social auth settings (Facebook)

SOCIAL_AUTH_DEFAULT_USERNAME = 'new_social_auth_user'
SOCIAL_AUTH_UID_LENGTH = 16
SOCIAL_AUTH_ASSOCIATION_HANDLE_LENGTH = 16
SOCIAL_AUTH_NONCE_SERVER_URL_LENGTH = 16
SOCIAL_AUTH_ASSOCIATION_SERVER_URL_LENGTH = 16
SOCIAL_AUTH_ASSOCIATION_HANDLE_LENGTH = 16
SESSION_SERIALIZER = 'django.contrib.sessions.serializers.PickleSerializer'

AUTHENTICATION_BACKENDS = (
    'social_auth.backends.facebook.FacebookBackend',
    'django.contrib.auth.backends.ModelBackend',
)

FACEBOOK_APP_ID = '326981494179278'
FACEBOOK_API_SECRET = 'f30845d0609004c5fc28917d24338919'
FACEBOOK_REDIRECT_URI = 'http://localhost:8080/'

SOCIAL_AUTH_ENABLED_BACKENDS = ('facebook', )

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'simpleSO.urls'

WSGI_APPLICATION = 'simpleSO.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'stackoverflow',
        'USER': 'denis',
        'PASSWORD': 'xjbc1u64',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Template files

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'templates',),
    os.path.join(BASE_DIR, 'questions/templates',),
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'social_auth.context_processors.social_auth_by_type_backends',
    'django.contrib.auth.context_processors.auth',
)

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static',),
)

LOGIN_REDIRECT_URL = '/'
