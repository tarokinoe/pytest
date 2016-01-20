# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [('testapp', '0016_auto_20160105_1024'), ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='questions',
            field=models.ManyToManyField(to='testapp.Question',
                                         through='testapp.GameQuestion'), ),
        migrations.AlterField(
            model_name='gamequestion',
            name='question',
            field=models.ForeignKey(to='testapp.Question'), ),
    ]
