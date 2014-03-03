from utils import LOCAL
import dj_database_url
SITE_ID = 1

DEBUG = False
TEMPLATE_DEBUG = DEBUG
SERVE_MEDIA = False

MEDIA_SERVER_URL = 'http://sdpm.arruda.blog.br'
MEDIA_URL = MEDIA_SERVER_URL+'/media/'
STATIC_URL = MEDIA_SERVER_URL+'/static/'

DATABASES = {
             'default': dj_database_url.config(default='postgres://localhost')
             }