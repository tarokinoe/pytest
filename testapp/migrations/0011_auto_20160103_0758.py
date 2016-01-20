# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [('testapp', '0010_auto_20151230_1755'), ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='tests',
            field=models.ManyToManyField(to='testapp.Test',
                                         through='testapp.Game'), ),
        migrations.AlterUniqueTogether(
            name='game',
            unique_together=set([('test', 'player')]), ),
    ]
