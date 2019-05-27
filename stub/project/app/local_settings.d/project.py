import os
ALLOWED_HOSTS = ['*']
STATIC_URL = '/static/'
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATICFILES_DIRS = [
#    os.path.join(BASE_DIR, "static"), # your static/ files folder
]
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTOCOL', 'https')
