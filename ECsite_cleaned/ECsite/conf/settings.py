"""
Django settings for conf project.

Generated by 'django-admin startproject' using Django 3.2.8.

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
SECRET_KEY = 'django-insecure-jxr$%t8^z^$gu1r)s0zz^th+++tex6!ntnc$@n!-mkfnp=fba-'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'accounts.apps.AccountsConfig',
    'products.apps.ProductsConfig',
    'shop.apps.ShopConfig',
    'contacts.apps.ContactsConfig',
    'cart.apps.CartConfig',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
]

AUTH_USER_MODEL = 'accounts.CustomUser'
ACCOUNT_FORMS = {"signup": "accounts.forms.SignupForm"}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'conf.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / "templates",
                 BASE_DIR / "templates"/"allauth",
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

WSGI_APPLICATION = 'conf.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases
"""
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'ecsite',
        'USER': 'postgres',
        'PASSWORD': 'postgres2003',
        'HOST': 'localhost',
        'PORT': '',
    }
}
"""
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'mydatabase',
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

LANGUAGE_CODE = 'ja'

TIME_ZONE = 'Asia/Tokyo'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / "static"]

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

MEDIA_URL = "/media/"
if DEBUG:
    MEDIA_ROOT = BASE_DIR / "media"

#################django-allauthでのメール認証設定ここから###################

# #djangoallauthでメールでユーザー認証する際に必要になる認証バックエンド
AUTHENTICATION_BACKENDS = [
    "django.contrib.auth.backends.ModelBackend",
    "allauth.account.auth_backends.AuthenticationBackend",
]

#ログイン時の認証方法はemailとパスワードとする
ACCOUNT_AUTHENTICATION_METHOD = "email"

#ログイン時にユーザー名(ユーザーID)は使用しない
ACCOUNT_USERNAME_REQUIRED = "False"

#ユーザー登録時に入力したメールアドレスに、確認メールを送信する事を必須(mandatory)とする
ACCOUNT_EMAIL_VERIFICATION = "mandatory"

#ユーザー登録画面でメールアドレス入力を要求する(True)
ACCOUNT_EMAIL_REQUIRED = True

#【加筆】2021年ぐらいにSendgridはユーザー名とパスワードによるメール送信を拒否するようになったため、上記のやり方は通用しない。下記にAPIキーを指定する
#詳細:https://noauto-nolife.com/post/django-sendgrid/

# EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
# DEFAULT_FROM_EMAIL = "ここにデフォルトの送信元メールアドレスを指定"

# SENDGRID_API_KEY = "ここにsendgridのAPIkeyを記述する"

#DEBUGがTrueのとき、メールの内容は全て端末に表示させる
if DEBUG:
    EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

#CHECK:認証時のメールの本文等の編集は templates/allauth/account/email/ から行うことができる

#################django-allauthでのメール認証設定ここまで###################

#django-allauth関係。django.contrib.sitesで使用するSITE_IDを指定する
SITE_ID = 1

#django-allauthログイン時とログアウト時のリダイレクトURL
LOGIN_REDIRECT_URL = '/shop/'
ACCOUNT_LOGOUT_REDIRECT_URL = '/account/login/'

LOGIN_URL = '/account/login/'
