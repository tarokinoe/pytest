# -*- encoding: utf-8 -*-

from django.core.management.base import BaseCommand
from django.core.management.base import CommandError
from tgmbot.bot import bot


class Command(BaseCommand):
    help = 'Run bot'

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        bot.polling(none_stop=True)
