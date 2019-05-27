CELERY_BROKER_URL = 'amqp://mq_user:mq_password@rabbitmq:5672/'
CELERY_RESULT_BACKEND = 'django-db'

if 'django_celery_results' not in INSTALLED_APPS:
  INSTALLED_APPS += ['django_celery_results']
