# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [('testapp', '0019_auto_20160107_0748'), ]

    operations = [
        migrations.AlterField(
            model_name='gamequestion',
            name='game',
            field=models.ForeignKey(related_name='game_questions',
                                    to='testapp.Game'), ),
    ]
