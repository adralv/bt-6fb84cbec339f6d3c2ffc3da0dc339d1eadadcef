import os
import sys
import logging
import traceback
from django.core.wsgi import get_wsgi_application

# Set the settings module for the project
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'clubhouse.settings')

# Setup logging for WSGI errors
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

try:
	# Get the WSGI application
	application = get_wsgi_application()
except Exception:
    logger.error('WSGI failed to start', exc_info=True)
    traceback.print_exc()