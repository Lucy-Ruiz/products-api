# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-xt)+mzblvs&_cllrg_4n&j(af!n$2osgw7oruu8uz@77r4ff7c'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'mysql.connector.django',
        'NAME': 'products_api_database',
        'USER': 'root',
        'PASSWORD': 'qazwsx2022',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'OPTIONS': {
            'autocommit': True
        }
    }
}

