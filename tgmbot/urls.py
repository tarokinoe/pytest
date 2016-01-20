from django.conf.urls import include, url
from django.conf import settings
from . import views
import re
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    url(re.escape(settings.TGM_BOT_TOKEN) + r'/$', csrf_exempt(views.webhook), name="webhook"),
]
