"""
Django settings for p project.

Generated by 'django-admin startproject' using Django 5.0.6.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-)ci1su+bga#d)k5b$yq)^1w*cmo-#kux9d@%)&0ssyb(-9s!+_'

AWS_COGNITO_REGION = 'af-south-1'
AWS_COGNITO_USER_POOL_ID = 'af-south-1_3ogEVC8W6'
AWS_COGNITO_APP_CLIENT_ID = '1qa3ngvpha1hcge9arintssh30'
AWS_COGNITO_APP_CLIENT_SECRET = '8u4alc94vr3pdn67tbal25eu1pk4colfs2t9g9id6ato7o90ts1'
AWS_COGNITO_REDIRECT_URL = 'https://ec2-13-247-145-14.af-south-1.compute.amazonaws.com:8000/bee/home'
AWS_COGNITO_LOGOUT_URL = 'https://localhost:8000/cognito/logout/'
AWS_COGNITO_JWK_URL = f'https://cognito-idp.{AWS_COGNITO_REGION}.amazonaws.com/{AWS_COGNITO_USER_POOL_ID}/.well-known/jwks.json'


# Add your AWS Cognito User Pool's JWK URL to your settings
AWS_COGNITO_JWK_URL = f'https://cognito-idp.{AWS_COGNITO_REGION}.amazonaws.com/{AWS_COGNITO_USER_POOL_ID}/.well-known/jwks.json'
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['bee-xj6g.onrender.com', 'ec2-13-247-145-14.af-south-1.compute.amazonaws.com']


# Application definition

INSTALLED_APPS = [
    'bee',
    'crispy_forms',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',  # Ensure this is before your custom middleware
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'bee.middleware.CognitoMiddleware',  # Your custom middleware should be after SessionMiddleware
]


LOGIN_URL = 'login'
LOGIN_REDIRECT_URL = 'index'
LOGOUT_REDIRECT_URL = 'index'

ROOT_URLCONF = 'p.p.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'p.wsgi.application'

CRISPY_TEMPLATE_PACK = 'bootstrap4'
CRISPY_ALLOWED_TEMPLATE_PACKS = 'bootstrap5'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = '/static/'


STATIC_ROOT = BASE_DIR / 'staticfiles'


STATICFILES_DIRS = [
    BASE_DIR / 'bee/static',
]



# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
