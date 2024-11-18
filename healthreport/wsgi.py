"""
WSGI config for healthreport project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""

import os
import sys

# Add your project directory to the sys.path
project_home = '/home/madinadairova05/mysite'
if project_home not in sys.path:
    sys.path.append(project_home)

# Set the Django settings module
os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'

# Activate your virtual environment
activate_env = os.path.expanduser('/home/madinadairova05/.virtualenvs/myenv/bin/activate_this.py')
with open(activate_env) as f:
    exec(f.read(), {'__file__': activate_env})

# Import Django and start the application
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
