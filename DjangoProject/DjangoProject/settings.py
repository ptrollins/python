"""
Django settings for DjangoProject project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""
# for language support
from django.utils.translation import ugettext_lazy as _
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '4fx9oigz%(2l#^@h6l2qs&dsa0b)qn4s+9azw3wvon(!n6z_l9'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

BOWER_COMPONENTS_ROOT = os.path.join(BASE_DIR, 'components')

BOWER_PATH = '/usr/local/bin/bower'

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'djangobower.finders.BowerFinder',
)


TEMPLATE_DIRS = (
    os.path.join(BASE_DIR,  'templates'),
)

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'dashboard',
    'registration',
    'djangobower',
    'django_nvd3',
)

BOWER_INSTALLED_APPS = (
    'jquery',
    'underscore',
    'nvd3'
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.locale.LocaleMiddleware',
)

ROOT_URLCONF = 'DjangoProject.urls'

WSGI_APPLICATION = 'DjangoProject.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'dashboard.db'),
    }
}

AUTH_USER_MODEL = 'dashboard.User'

REGISTRATION_OPEN = True            # If True, users can register
ACCOUNT_ACTIVATION_DAYS = 7         # One-week activation window; you may, of course, use a different value.
REGISTRATION_AUTO_LOGIN = True      # If True, the user will be automatically logged in.
LOGIN_REDIRECT_URL = '/dashboard/'  # The page you want users to arrive at after they successful log in
LOGIN_URL = '/accounts/login/'      # The page users are directed to if they are not logged in,
                                    # and are trying to access pages requiring authentication

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

# added for multilingual support
LANGUAGES = (('en', _('English')),
             ('fr', _('French')),)

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


