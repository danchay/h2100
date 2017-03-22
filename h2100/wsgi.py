"""
<<<<<<< HEAD
WSGI config for instance project.
=======
WSGI config for h2100 project.
>>>>>>> b75520b83bcaadb1db75cd390a3c3fd4da760c11

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application


from whitenoise.django import DjangoWhiteNoise

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "h2100.settings.production")

application = get_wsgi_application()
application = DjangoWhiteNoise(application)

