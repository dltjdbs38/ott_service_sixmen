"""
Django settings for config project.

Generated by 'django-admin startproject' using Django 3.2.6.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""
import os
from pathlib import Path
import datetime
# drf <-> 리엑트 연동 https://this-programmer.tistory.com/135

env = os.environ

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret! 
SECRET_KEY = env.get("DJANGO_SECRET_KEY", default="secret key here") 
# print(SECRET_KEY) 
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [] # ALLOWED_HOSTS 는 원하는 호스트가 접근할 수 있도록 설정
# ( * 은 모든 호스트가 접근 가능합니다)

APPEND_SLASH=False
#react의 경우 SPA라 /가 필요 없는데, 원래 True로 자동 설정이라
#이렇게 주소 접근하면 페이지를 찾을 수 없기 때문에.

# CORS
# 1. 배포용일 경우 'google.com' , 'hostname.example.com' 등
CORS_ORIGIN_WHITELIST = ['http://127.0.0.1:3000', 'http://localhost:3000', 'http://127.0.0.1:8000']
# 2. 개발일 경우
# CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = True

# Application definition

REST_FRAMEWORK={
    'DEFAULT_PERMISSION_CLASSES':[
        'rest_framework.permissions.IsAuthenticated',
        'rest_framework.permissions.AllowAny',
        #첫번째는 인증된 회원만, 두번째는 모든 사람 접근 허용.
    ],
    'DEFAULT_AUTHENTICATION_CLASSES':(
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
    #api가 실행 됐을때 인증할 클래스를 정의.
    #jwt로 인증을 할거니까 api가 실행되면 jwt로 인증을 실행.
    ),
}

JWT_AUTH={
    'JWT_SECRET_KEY':SECRET_KEY,#비밀키 설정
    'JWT_ALGORITHM':'HS256',#암호화 알고리즘
    'JWT_VERIFY_EXPIRATION':True,#토큰 검증
    'JWT_ALLOW_REFRESH':True,#유효기간에 딸느 새로운 토큰 반환
    'JWT_EXPIRATION_DELTA':datetime.timedelta(minutes=30),#access토큰 만료시간
    'JWT_REFRESH_EXPIRATION_DELTA':datetime.timedelta(days=3),#refresh토큰 만료시간.
    'JWT_RESPONSE_PAYLOAD_HANDLER':'api.custom_responses.my_jwt_response_handler',
    #?
    'JWT_RESPONSE_PAYLOAD_HANDLER':'rest_framework_jwt.utils.jwt_response_payload_handler'
}



INSTALLED_APPS = [
    'apps.user',
    'apps.small_theater',
    'rest_framework',
    'rest_framework_jwt',
    'corsheaders',
    'drf_yasg',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

# REST_FRAMEWORK ={ # 블로그 보고 추가한 부분
#     'DEFAULT_PERMISSION_CLASSES': [
#         'rest_framework.permissions.AllowAny',
#     ]
# }

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware', # CORS 추가
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware', # 추가
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# 리엑트랑 장고 같이 돌리기 이제부터는 frontend요청을 처리할 웹서버와 backend api요청을 처리할 두 개의 웹서버가 작동돼야한다. 
# 장고 : project-template/backend$ python3 manage.py runserver
# 리엑트 : project-template/frontend$ yarn start
# 리엑트가 받을 때 const response = await fetch('http://127.0.0.1:8000/small-theater');
# const 변수 = await response.json();


ROOT_URLCONF = 'config.urls'
AUTH_USER_MODEL = 'user.User'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS' : [],
        # 'DIRS': [
        #     os.path.join(BASE_DIR / 'templates'),
        # ], #templates안에 app에 관한 html들
        # 'DIRS' : [
        #     os.path.join(BASE_DIR, 'frontend','build'), #장고템플릿X 리엑트템플릿O 경로변경
        # ],
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

#리엑트템플릿 경로추가
# STATICFILES_DIRS = [
#     os.path.join(BASE_DIR, 'frontend', 'build', 'static'),
# ]


WSGI_APPLICATION = 'config.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

DATABASES = {
    'default' : {
        'ENGINE': 'django.db.backends.mysql', 
        'NAME': 'ott_service_database2',  # DB이름                
        'USER': 'seoyoon1', # DB로그인 유저명                          
        'PASSWORD': 'seoyoon1234',  #DB로그인 비밀번호    
        'HOST': '172.22.103.66',  # 얘는 내 윈도우데스크탑 켜고끌때마다 바뀜                   
        'PORT': '3306',                          
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

# AUTH_USER_MODEL = 'user.User' # 속성은 User가 가지고 있는게 아니라 User가 상속받는 AbstractUser가 다 가지고 있다. 즉, User는 기능이 없는 깡통 수준이고, 장고 내부에 세팅된 값이라 변경도 불가능하다.

# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'ko-kr'
#영어에서 바꿈

TIME_ZONE = 'Asia/Seoul'
#시간 기준을 서울로 맞춤.

USE_I18N = True

USE_L10N = True

USE_TZ = False
# 이걸 False로 해야 우리나라 시간을 가져온다

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
