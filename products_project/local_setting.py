# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-d3z+1e+r6d959*3)(g1+2@lz4imh*)q4tmm0tu2l7s#%7%xr^q'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'products_database',
        'HOST': 'localhost',
        'USER': 'root',
        'PASSWORD': 'password'
    }
}
