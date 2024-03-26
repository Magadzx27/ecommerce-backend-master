# """
# Django settings for newone project.

# Generated by 'django-admin startproject' using Django 3.0.6.

# For more information on this file, see
# https://docs.djangoproject.com/en/3.0/topics/settings/

# For the full list of settings and their values, see
# https://docs.djangoproject.com/en/3.0/ref/settings/
# """

# import os
# import datetime
# import sys


# # Build paths inside the project like this: os.path.join(BASE_DIR, ...)
# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# # Quick-start development settings - unsuitable for production
# # See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# # SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = '-(9$5+_w@dm4xs=nr&mz426*x+%_337ev6v#!ydkd)4373-=()'

# # SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = False
# SECURE_HSTS_SECONDS = 36000
# SESSION_COOKIE_SECURE = True
# SECURE_HSTS_INCLUDE_SUBDOMAINS = True
# SECURE_SSL_REDIRECT = True
# CSRF_COOKIE_SECURE = True
# SECURE_HSTS_PRELOAD = True

# ALLOWED_HOSTS = [
#     'localhost',
#     'smartpc.filbert.ai',
#     'admin.aicompumall.com'
#     'aicompumall.com'
# ]
# CORS_ORIGIN_WHITELIST = (
#     'https://admin.aicompumall.com',
#     'https://aicompumall.com',
#     'https://www.admin.aicompumall.com',
#     'https://www.aicompumall.com'
# )

# AUTH_USER_MODEL = 'authentication.User'

# # Application definition

# INSTALLED_APPS = [
#     'django.contrib.admin',
#     'django.contrib.auth',
#     'django.contrib.contenttypes',
#     'django.contrib.sessions',
#     'django.contrib.messages',
#     'django.contrib.staticfiles',
#     'rest_framework',
#     'authentication',
#     'rest_framework.authtoken',
#     'corsheaders',
#     'drf_yasg',
#     'phonenumber_field',
#     'products',
#     'categories',
#     'templates',
#     'rest_framework_simplejwt.token_blacklist',
#     'carts',
#     'imageSlider',
#     'aboutus',
#     'file_uploader',
#     'product_review',
#     'payment',
#     'payment_method',
#     'orders',
#     'order_item',
#     'shipping',
#     'shipping_method',
#     'django_countries',
# ]

# MIDDLEWARE = [
#     'django.middleware.security.SecurityMiddleware',
#     'django.contrib.sessions.middleware.SessionMiddleware',
#     'corsheaders.middleware.CorsMiddleware',
#     'django.middleware.common.CommonMiddleware',
#     'django.middleware.csrf.CsrfViewMiddleware',
#     'django.contrib.auth.middleware.AuthenticationMiddleware',
#     'django.contrib.messages.middleware.MessageMiddleware',
#     'django.middleware.clickjacking.XFrameOptionsMiddleware',
# ]

# SWAGGER_SETTINGS = {
#     'SECURITY_DEFINITIONS': {
#         'Bearer': {
#             'type': 'apiKey',
#             'name': 'Authorization',
#             'in': 'header'
#         }
#     }
# }

# ROOT_URLCONF = 'newone.urls'

# TEMPLATES = [
#     {
#         'BACKEND': 'django.template.backends.django.DjangoTemplates',
#         'DIRS': [os.path.join(BASE_DIR, "templates")],
#         'APP_DIRS': True,
#         'OPTIONS': {
#             'context_processors': [
#                 'django.template.context_processors.debug',
#                 'django.template.context_processors.request',
#                 'django.contrib.auth.context_processors.auth',
#                 'django.contrib.messages.context_processors.messages',
#             ],
#         },
#     },
# ]

# WSGI_APPLICATION = 'newone.wsgi.application'


# # Database
# # https://docs.djangoproject.com/en/3.0/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'filbmlxi_aicompumall',
#         'USER': 'filbmlxi_aicompumall',
#         'PASSWORD': 'aicompumall',
#         'HOST': '127.0.0.1',
#         'PORT': '3306',
#     }
# }

# REST_FRAMEWORK = {
#     'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
#     'PAGE_SIZE': 50,
#     'NON_FIELD_ERRORS_KEY': 'error',
#     'DEFAULT_AUTHENTICATION_CLASSES': (
#         'rest_framework_simplejwt.authentication.JWTAuthentication',
#     )
# }


# SIMPLE_JWT = {
#     'ACCESS_TOKEN_LIFETIME': datetime.timedelta(minutes=120),
#     'REFRESH_TOKEN_LIFETIME': datetime.timedelta(days=1),
# }

# # Password validation
# # https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

# AUTH_PASSWORD_VALIDATORS = [
#     {
#         'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
#     },
#     {
#         'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
#     },
#     {
#         'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
#     },
#     {
#         'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
#     },
# ]

# MEDIA_URL = '/media/'
# MEDIA_ROOT = os.path.join(BASE_DIR, "../media")
# # Internationalization
# # https://docs.djangoproject.com/en/3.0/topics/i18n/

# LANGUAGE_CODE = 'en-us'

# TIME_ZONE = 'Asia/Kuala_Lumpur'

# USE_I18N = True

# USE_L10N = True

# USE_TZ = True

# # Static files (CSS, JavaScript, Images)
# # https://docs.djangoproject.com/en/3.0/howto/static-files/

# STATIC_URL = '/static/'
# STATIC_ROOT = os.path.join(BASE_DIR, '../static/')

# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_USE_TLS = True
# EMAIL_HOST = 'smtp.stackmail.com'
# EMAIL_PORT = 587
# EMAIL_HOST_USER = "bot@aicompumall.com"
# EMAIL_HOST_PASSWORD = "bot@aicompumall.com"
# DEFAULT_FROM_EMAIL = "bot@aicompumall.com"
