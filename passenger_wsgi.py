import os, sys
sys.path.insert(0, '/var/www/u2036297/data/www/tangatarov.com/mektep')
sys.path.insert(1, '/var/www/u2036297/data/env/lib/python3.10/site-packages')
os.environ['DJANGO_SETTINGS_MODULE'] = 'mektep.settings'
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
