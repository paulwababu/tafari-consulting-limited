"""
Django settings for DjangoUploadModelForm project.

Generated by 'django-admin startproject' using Django 2.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE_DIR = os.path.join(BASE_DIR,"templates")
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'qap$6$cd*v*i#rvef&q&7%j%4dk36z0u^j&y(%^dq!ieb1pm*s'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'crispy_forms',
    'tutorials.apps.TutorialsConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'csp.middleware.CSPMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'DjangoUploadModelForm.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATE_DIR],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'DjangoUploadModelForm.wsgi.application'

# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
   'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'testdb',
        'USER': 'paulsaul',
        'PASSWORD': '443556126216621',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}

# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Africa/Nairobi'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'files')

MEDIA_URL = '/files/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]


LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'

CRISPY_TEMPLATE_PACK="bootstrap4"
#Security
CSRF_COOKIE_SECURE = True #to avoid transmitting the CSRF cookie over HTTP accidentally.
SESSION_COOKIE_SECURE = True #to avoid transmitting the session cookie over HTTP accidentally.

SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True

SECURE_SSL_REDIRECT = True

SECURE_HSTS_SECONDS = 15780000  # 1 day
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True
#Add the following lines to settings.py
# Content Security Policy
CSP_DEFAULT_SRC = ("'none'", )
CSP_BASE_URI = ("'none'", )
CSP_STYLE_SRC = ("'unsafe-inline'", "'self'", 'maxcdn.bootstrapcdn.com', 'paulkiragu621.github.io', 'fonts.googleapis.com', 'stackpath.bootstrapcdn.com')
CSP_SCRIPT_SRC = ("'self'", 'ajax.googleapis.com', 'paulkiragu621.github.io', 'stackpath.bootstrapcdn.com')
CSP_IMG_SRC = ("'self'", 'icomnalt.sirv.com', 'colormatemedia.com')
CSP_FONT_SRC = ("'self'", 'maxcdn.bootstrapcdn.com', 'stackpath.bootstrapcdn.com', 'fonts.gstatic.com', 'paulkiragu621.github.io', 'fonts.googleapis.com')
CSP_INCLUDE_NONCE_IN = ("script-src")
CSP_FRAME_SRC = ["https://www.google.com"]
CSP_SCRIPT_SRC_ELEM = ("'self'", "'unsafe-inline'", 'stackpath.bootstrapcdn.com', 'cdnjs.cloudflare.com', 'ajax.googleapis.com')
CSP_CONNECT_SRC = ("'self'", "'unsafe-inline'")
CSP_STYLE_SRC_ELEM = ("'self'","'unsafe-inline'", 'paulkiragu621.github.io','fonts.googleapis.com', 'getbootstrap.com', 'stackpath.bootstrapcdn.com')
