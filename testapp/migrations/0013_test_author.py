# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [('testapp', '0012_game_state'), ]

    operations = [
        migrations.AddField(model_name='test',
                            name='author',
                            field=models.CharField(max_length=200,
                                                   verbose_name=b'Author',
                                                   blank=True), ),
    ]
