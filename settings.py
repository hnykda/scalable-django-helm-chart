import os

PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY', 'xxx')

INSTALLED_APPS = [
    'django.contrib.admin',
    'rest_framework.authtoken',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

CACHE_LOCATION = os.getenv('DJANGO_APP_CACHE_LOCATION', 'wonderland').split()
CACHES = {
    "default": {
        "BACKEND": os.getenv('DJANGO_APP_CACHE_BACKEND',
                             'django.core.cache.backends.locmem.LocMemCache'),
        # e.g. redis backend supports multiple locations in list (for replicas), 
        # while e.g. LocMemCache needs only a string
        "LOCATION": CACHE_LOCATION[0] if len(CACHE_LOCATION) == 1 else CACHE_LOCATION, 
    }
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


ROOT_URLCONF = 'djangoapp.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(PROJECT_DIR, 'templates'),
        ],
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

WSGI_APPLICATION = 'djangoapp.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.' + os.environ.get('DJANGO_APP_DB_ENGINE', 'sqlite3'),
        'NAME': os.environ.get('DJANGO_APP_DB_NAME', os.path.join(BASE_DIR, 'db.sqlite3')),
        'USER': os.environ.get('DJANGO_APP_DB_USER'),
        'HOST': os.environ.get('DJANGO_APP_DB_HOST'),
        'PORT': os.environ.get('DJANGO_APP_DB_PORT'),
        'PASSWORD': os.environ.get('DJANGO_APP_DB_PASSWORD'),
        'CONN_MAX_AGE': 600,
    }
}

SESSION_ENGINE = 'django.contrib.sessions.backends.cached_db'
SESSION_CACHE_ALIAS = "default"

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
LOGIN_REDIRECT_URL = 'index'

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

### STATIC FILES
STATICFILES_DIRS = [
    os.path.join(PROJECT_DIR, "static"),
]

STATIC_ROOT = os.environ.get('STATIC_ROOT', os.path.join(BASE_DIR, 'static'))

STATIC_URL = os.getenv('DJANGO_APP_STATIC_URL', '/static/')
