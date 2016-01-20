# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [('testapp', '0004_auto_20151228_1133'), ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='stop_on',
            field=models.DateTimeField(null=True,
                                       verbose_name=b'when was stoped',
                                       blank=True), ),
    ]
