"""

Django production settings for davidchuka project.



Generated by 'django-admin startproject' using Django 2.0.2.

"""



import os

from dotenv import load_dotenv



# Build paths inside the project like this: os.path.join(BASE_DIR, ...)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))





# Load .env file

load_dotenv(os.path.join(BASE_DIR, '.env'))



# Quick-start development settings - unsuitable for production

# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/



SECRET_KEY = os.getenv('DJANGO_SECRET_KEY')



DEBUG = True


print(os.getenv('DJANGO_ALLOWED_HOSTS').split(","))
ALLOWED_HOSTS = [] or os.getenv('DJANGO_ALLOWED_HOSTS').split(",")



SITE_ID = 1



# Application definition

INSTALLED_APPS = [


    'django.contrib.admin',

    'django.contrib.auth',

    'django.contrib.contenttypes',

    'django.contrib.sessions',

    'django.contrib.messages',

    'django.contrib.staticfiles',

    'django.contrib.sites',

    'django.contrib.sitemaps',

    'info.apps.InfoConfig',

    'blog.apps.BlogConfig',

    'projects.apps.ProjectsConfig',

    'store.apps.StoreConfig',

    'django_extensions',

    'django_summernote',

    'django_heroku',

    'sorl.thumbnail',

    'taggit'

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



ROOT_URLCONF = 'davidchuka.urls'



TEMPLATES = [

    {

        'BACKEND': 'django.template.backends.django.DjangoTemplates',

        'DIRS': ['templates'],

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



#EMAIL CONFIGURARTION

#EMAIL_HOST = 'smtp.gmail.com'

#EMAIL_HOST_USER = 'davidnwadiogbu@gmail.com'

EMAIL_HOST = 'localhost'

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

#EMAIL_PORT = 25

#EMAIL_USE_TLS = True



WSGI_APPLICATION = 'davidchuka.wsgi.application'





# Database

# https://docs.djangoproject.com/en/2.0/ref/settings/#databases



import dj_database_url



DATABASES = {

    'default': dj_database_url.config()

}



# Password validation

# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators



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

# https://docs.djangoproject.com/en/2.0/topics/i18n/



LANGUAGE_CODE = 'en-NG'



TIME_ZONE = "Africa/Lagos"



USE_I18N = True



USE_L10N = True



USE_TZ = True





# Static files (CSS, JavaScript, Images)

# https://docs.djangoproject.com/en/2.0/howto/static-files/





STATIC_URL = '/static/'

STATIC_ROOT = os.getenv('STATIC_ROOT', os.path.join(BASE_DIR, 'static'))

STATICFILES_DIRS = [os.path.join(BASE_DIR, 'davidchuka/static'), ]

MEDIA_ROOT = os.getenv('MEDIA_ROOT', os.path.join(BASE_DIR, 'media'))

MEDIA_URL = '/media/'


STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'



# try:

#     from .local_settings import *

# except ImportError:

#     pass


