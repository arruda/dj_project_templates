from utils import LOCAL
import dj_database_url
SITE_ID = 1

DEBUG = False
TEMPLATE_DEBUG = DEBUG
SERVE_MEDIA = False


# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Allow all host headers
ALLOWED_HOSTS = ['*']

DATABASES = {
             'default': dj_database_url.config(default='postgres://localhost')
             }
