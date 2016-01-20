# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0005_auto_20151228_1140'),
    ]

    operations = [
        migrations.AddField(
            model_name='test',
            name='published',
            field=models.BooleanField(default=False, verbose_name=b'is published'),
        ),
        migrations.AlterField(
            model_name='question',
            name='published',
            field=models.BooleanField(default=True, verbose_name=b'is published'),
        ),
    ]
