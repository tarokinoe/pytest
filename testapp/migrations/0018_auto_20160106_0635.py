# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [('testapp', '0017_auto_20160106_0448'), ]

    operations = [
        migrations.RenameField(model_name='answer',
                               old_name='answer',
                               new_name='text', ),
        migrations.AlterField(model_name='game',
                              name='player',
                              field=models.ForeignKey(related_name='games',
                                                      to='testapp.Player'), ),
    ]
