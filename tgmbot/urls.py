import re

from django.conf import settings
from django.conf.urls import include
from django.conf.urls import url
from django.views.decorators.csrf import csrf_exempt

from . import views

urlpatterns = [
    url(
        re.escape(settings.TGM_BOT_TOKEN) + r'/$',
        csrf_exempt(views.webhook),
        name='webhook'),
]
