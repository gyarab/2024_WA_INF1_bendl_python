"""
Django 5.1.6.

more info:
https://docs.djangoproject.com/en/5.1/topics/settings/
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

from pathlib import Path
import os
import socket

current_hostname = socket.gethostname()


BASE_DIR = Path(__file__).resolve().parent.parent

FIXTURE_DIRS = [BASE_DIR / "fixtures/"]

MEDIA_URL = '/media/' #'/var/caddy.root.d/dasiha.svs.gyarab.cz/media/'
MEDIA_ROOT = BASE_DIR / 'media' # MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Static files https://docs.djangoproject.com/en/5.1/howto/static-files/
STATIC_URL = 'static/'
STATICFILES_DIRS = [
    BASE_DIR / "static",
]


# Default primary key field type https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/
# SECURITY WARNING: keep the secret key used in production secret! Tak pardón
SECRET_KEY = 'g0!-xt$_z2=71sfjiz$&ma5h@%2@p=o^es^s=dnsy@@%-q!n(%'

# DEBUG shouldn´t be set to True in production!
if current_hostname == "avava":
    DEBUG = False
else:
    DEBUG = True
########################------Logs-------#############################
LOG_DIR = os.path.join(BASE_DIR, 'logs')
os.makedirs(LOG_DIR, exist_ok=True)  # Ensure the log directory exists

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,  # Keeps Django's default loggers
    'formatters': {
        'verbose': {
            'format': '{asctime} [{levelname}] {name} - {message}',
            'style': '{',
        },
    },
    'handlers': {
        'file': {
            'level': 'ERROR',  # You can change to DEBUG/INFO/WARNING as needed
            'class': 'logging.FileHandler',
            'filename': os.path.join(LOG_DIR, 'errors.log'),
            'formatter': 'verbose',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'ERROR',
            'propagate': True,
        },
        'django.request': {
            'handlers': ['file'],
            'level': 'ERROR',
            'propagate': False,
        },
    },
}

ALLOWED_HOSTS = ["dasiha.svs.gyarab.cz", "127.0.0.1", ]
CSRF_TRUSTED_ORIGINS = [
    "https://dasiha.svs.gyarab.cz",
]
CSRF_COOKIE_SECURE = True

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'social_django',
    'crispy_forms',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'content.apps.ContentConfig',
    'library',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'social_django.middleware.SocialAuthExceptionMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

AUTHENTICATION_BACKENDS = (
    'social_core.backends.google.GoogleOAuth2',
    'django.contrib.auth.backends.ModelBackend',
)

ROOT_URLCONF = 'cms.urls'

LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'

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

WSGI_APPLICATION = 'cms.wsgi.application'

# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

if current_hostname == "avava":
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'db4136',
            'USER': 'db4136',
            'PASSWORD': '',
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }


print(f"Using database settings for {current_hostname}: {DATABASES['default']}")

# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

