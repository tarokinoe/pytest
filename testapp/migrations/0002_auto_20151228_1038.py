# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [('testapp', '0001_initial'), ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='answer_description',
            field=models.TextField(max_length=20000,
                                   verbose_name=b'Answer description',
                                   blank=True), ),
    ]
