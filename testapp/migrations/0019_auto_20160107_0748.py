# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [('testapp', '0018_auto_20160106_0635'), ]

    operations = [
        migrations.RemoveField(model_name='gamequestion',
                               name='answer', ),
        migrations.AddField(
            model_name='gamequestion',
            name='player_answer',
            field=models.CharField(max_length=1,
                                   verbose_name=b'Player answer',
                                   blank=True), ),
        migrations.AddField(
            model_name='gamequestion',
            name='right_answer',
            field=models.CharField(max_length=1,
                                   verbose_name=b'Letter of right answer',
                                   blank=True), ),
    ]
