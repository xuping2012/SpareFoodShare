"""
Django settings for SpareFoodShare project.

Generated by 'django-admin startproject' using Django 3.2.12.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-pth+zswy7mhe40+9wif0!4l@tvmm#%^n^rj2n7e17=nn4p0m4k'

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

    #local
    'SpareFoodShare',
    'payments',
    'shop',
    'channels',
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

ROOT_URLCONF = 'SpareFoodShare.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'], # new
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

WSGI_APPLICATION = 'SpareFoodShare.wsgi.application'
ASGI_APPLICATION = 'SpareFoodShare.asgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.sqlite3',
#        'NAME': BASE_DIR / 'db.sqlite3',
#    }
#}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',  # 默认
        'NAME': 'foodforshare1',  # 连接的数据库
        'HOST': '192.168.2.213',  # mysql的ip地址
        'PORT': 3306,  # mysql的端口
        'USER': 'root',  # mysql的用户名
        'PASSWORD': 'NbQNJwPjpOwQKDppsj5yneWR'  # mysql的密码：pdP2PEoOZSeiDrm6T280RE6k
    }
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

STATIC_URL = '/static/'

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'




STRIPE_PUBLISHABLE_KEY = 'pk_test_51KlAoYHe8GrBj22BBTiB8zigiihahrEG9WQOER5PX1cHxQOIakb7xbdudeX9LTwHPcrvLsokDDpD222bcL4xJfvN00BVs9O2eS'
STRIPE_SECRET_KEY = 'sk_test_51KlAoYHe8GrBj22BHf39bZYPHOa4MIguLAToPJ5PzW3BqMmAtNT6bABbr74rybUQu6OtfgXOMiJjcfsjcu41q6ne00KRqIy7gv'



STATIC_URL = '/static/'

STATICFILES_DIRS = [BASE_DIR / 'static']


CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG': {
            "hosts": [('192.168.2.213', 6379)],
        },
    },
}

AUTH_USER_MODEL = 'payments.Profile'


DEFAULT_FROM_EMAIL = 'example@example.com' # change this!
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
#LOGIN_URL = '/login'