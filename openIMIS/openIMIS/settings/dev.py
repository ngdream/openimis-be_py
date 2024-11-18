import os

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
# Set ALLOWED_HOSTS
ALLOWED_HOSTS = ['*']
CSRF_TRUSTED_ORIGINS = [
    'https://localhost',
    'https://192.168.0.1',
    'https://localhost:8000',
    'https://192.168.0.1:8000',
    'https://localhost:3000',
    'https://192.168.0.1:3000',
]
# Set CORS_ALLOWED_ORIGINS to match CSRF_TRUSTED_ORIGINS
CORS_ALLOWED_ORIGINS = CSRF_TRUSTED_ORIGINS

ASYNC = os.environ.get('ASYNC', False)
