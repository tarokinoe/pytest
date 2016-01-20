# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0002_auto_20151228_1038'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='questions',
            field=models.ManyToManyField(to='testapp.TestQuestion', through='testapp.GameQuestion'),
        ),
        migrations.AlterField(
            model_name='gamequestion',
            name='question',
            field=models.ForeignKey(to='testapp.TestQuestion'),
        ),
    ]
