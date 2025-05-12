"""
Django cv_project projesi için ayarlar.
"""

import os
from pathlib import Path

# Proje içindeki yolları şöyle oluştur: BASE_DIR / 'altdizin'
BASE_DIR = Path(__file__).resolve().parent.parent

# GÜVENLİK UYARISI: üretim ortamında kullanılan gizli anahtarı gizli tutun!
# Gerçek bir projede, bu çevre değişkenlerinden yüklenirdi
SECRET_KEY = 'django-insecure-cv-website-dev-key-change-in-production'

# GÜVENLİK UYARISI: üretim ortamında hata ayıklama modunu açık bırakmayın!
DEBUG = True

ALLOWED_HOSTS = ['localhost', '127.0.0.1', '0.0.0.0']

# Uygulama tanımları
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'cv_app',  # Bizim CV uygulamamız
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # Statik dosyaları sunmak için
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'cv_project.urls'

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

WSGI_APPLICATION = 'cv_project.wsgi.application'

# Veritabanı
# Geliştirme için basit SQLite veritabanı
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Şifre doğrulama
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

# Dil eklentilerimiz
LANGUAGE_CODE = 'tr-tr' 
TIME_ZONE = 'Europe/Istanbul'  
USE_I18N = True
USE_TZ = True

# Statik dosyalar (CSS, JavaScriptve Resimler)
STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

# Canlı ortamda statik dosyalar için WhiteNoise yapılandırması
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Varsayılan birincil anahtar alan türü
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'