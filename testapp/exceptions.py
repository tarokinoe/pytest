# -*- encoding: utf-8 -*-
from django.utils.translation import ugettext as _


class TestAppError(Exception):
    def __str__(self):
        return _('Error in test application')


class OpenGameAlreadyExists(TestAppError):
    def __str__(self):
        return _('Player already has open game.')
