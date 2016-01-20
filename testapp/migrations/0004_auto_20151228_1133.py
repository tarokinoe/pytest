# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [('testapp', '0003_auto_20151228_1131'), ]

    operations = [
        migrations.RenameModel(old_name='Gamers',
                               new_name='Player', ),
        migrations.RenameField(model_name='game',
                               old_name='gamer',
                               new_name='player', ),
    ]
