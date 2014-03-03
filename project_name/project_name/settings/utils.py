
import os

MAIN_APP_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DJANGO_ROOT = os.path.dirname(MAIN_APP_ROOT)
SITE_ROOT = os.path.dirname(DJANGO_ROOT)

LOCAL = lambda x: os.path.join(DJANGO_ROOT, x)

