"""
Django settings for shirtmonster project.

Generated by 'django-admin startproject' using Django 3.2.23.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path
import os
import dj_database_url

if os.path.isfile('env.py'):
	import env

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = "DEBUG" in os.environ

ALLOWED_HOSTS = [os.environ.get("DEV_URL"), os.environ.get("PROD_URL")]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
	'django.contrib.sites',
	'allauth',
	'allauth.account',
	'allauth.socialaccount',
    'django.contrib.staticfiles',
	'home',
    'storages',
    'products',
    'shop',
    'users',
    'cart',
    'wishlist',
    'checkout',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
	"allauth.account.middleware.AccountMiddleware",                                 # required by allauth
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'shirtmonster.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
			os.path.join(BASE_DIR, 'templates'),
			os.path.join(BASE_DIR, 'templates', 'allauth'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',                       # required by allauth
                'django.contrib.auth.context_processors.auth',                      # required by allauth
                'django.contrib.messages.context_processors.messages',
                'cart.contexts.cart_contents',                                      # registers the cart context processor 
            ],
        },
    },
]

MESSAGE_STORAGE = 'django.contrib.messages.storage.session.SessionStorage'          # stores messages in the session storage

# allauth settings
AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',                                    # Needed to login by username in Django admin, regardless of allauth
    'allauth.account.auth_backends.AuthenticationBackend',                          # Authentication methods specific to allauth such as login by email or username
)

SITE_ID = 1

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'                    # Required for console confirmation emails in dev mode
ACCOUNT_AUTHENTICATION_METHOD = 'username_email'                                    # Lets the user choose betwen username or email login
ACCOUNT_EMAIL_REQUIRED = True                                                       # Without an email users cant register
ACCOUNT_EMAIL_VERIFICATION = 'required'                                             # Unconfirmed users wont be set to active in the website
ACCOUNT_SIGNUP_EMAIL_ENTER_TWICE = True                                             # Confirm email in registration process (write twice)
ACCOUNT_USERNAME_MINLEGNTH = 4                                                      # Username cant be shorter than 4 characters
LOGIN_URL = '/accounts/login'                                                       # The url wef ind the login form
LOGIN_REDIRECT_URL = '/'                                                            # Sends user to the home page after log in

WSGI_APPLICATION = 'shirtmonster.wsgi.application'

#email settings
EMAIL_HOST = os.environ.get("EMAIL_HOST")
EMAIL_PORT = os.environ.get("EMAIL_PORT")
EMAIL_USE_TLS = os.environ.get("EMAIL_USE_TLS")
EMAIL_HOST_USER = os.environ.get("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = os.environ.get("EMAIL_HOST_PASSWORD")

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
	'default': dj_database_url.parse(os.environ.get("DATABASE_URL"))
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

# These are used in the local environment
STATIC_URL = '/static/'
STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static')),  
MEDIA_URL = '/media/'
MEDIA_ROOT  = os.path.join(BASE_DIR, 'media')

# Variables for order processing
FREE_DELIVERY_THRESHOLD = 150
STANDARD_DELIVERY_PERCENTAGE = 10
TAX_PERCENTAGE = 0.19

# AWS and dev config
if 'USE_AWS' in os.environ:
# Caching
    AWS_S3_OBJECT_PARAMETERS = {
        'Expires': 'Thu, 31 Dec 2099 20:00:00 GMT',
        'CacheControl': 'max-age=94608000'  
    }

# Bucket
    AWS_STORAGE_BUCKET_NAME = os.environ.get('AWS_BUCKET')
    AWS_S3_REGION_NAME = os.environ.get('AWS_REGION')
    AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY')
    AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_KEY')
    AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.{AWS_S3_REGION_NAME}.amazonaws.com'

# Static and Media files
    STATICFILES_STORAGE = 'custom_storages.StaticStorage'
    STATICFILES_LOCATION = 'static'
    DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'
    MEDIAFILES_LOCATION = 'media'

# Overrides for static and media files in prod
    STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{STATICFILES_LOCATION}/'
    MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{MEDIAFILES_LOCATION}/'


# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'