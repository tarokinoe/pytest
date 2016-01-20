from django.http import HttpResponse
from django.core.exceptions import PermissionDenied
from django.shortcuts import render
from django.conf import settings
from .bot import bot
import telebot


def webhook(request):
    import logging
    from pytest.settings.production import ADMINS
    if request.method == 'POST':
        if request.META['CONTENT_TYPE'] == 'application/json': 
            json_string = request.body
            update = telebot.types.Update.de_json(json_string)
            bot.process_new_messages([update.message])
            return HttpResponse()
    
    raise PermissionDenied
