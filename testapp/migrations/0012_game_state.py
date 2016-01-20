# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [('testapp', '0011_auto_20160103_0758'), ]

    operations = [
        migrations.AddField(model_name='game',
                            name='state',
                            field=models.CharField(default=b'O',
                                                   max_length=10,
                                                   verbose_name=b'Game state',
                                                   choices=[
                                                       (b'O', b'Open game'), (
                                                           b'C', b'Close game')
                                                   ]), ),
    ]
