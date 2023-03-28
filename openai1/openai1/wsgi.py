"""
WSGI config for openai1 project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/
"""

import os
import sys

sys.path.append('/home/myproject/openai1/openai1')
sys.path.append('/home/myproject/myvenv/lib/python3.11/site-packages')

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'openai1.settings')

from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()
