# -*- encoding: utf-8 -*-

import telebot
from django.conf import settings
from django.core.exceptions import PermissionDenied
from django.http import HttpResponse
from django.shortcuts import render

from .bot import bot


def webhook(request):
    from pytest.settings.production import ADMINS
    if request.method == 'POST':
        if request.META['CONTENT_TYPE'] == 'application/json':
            json_string = request.body
            update = telebot.types.Update.de_json(json_string)
            bot.process_new_messages([update.message])
            return HttpResponse()

    raise PermissionDenied
