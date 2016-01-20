# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0013_test_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='test',
            name='description',
            field=models.CharField(max_length=2000, verbose_name=b'Description', blank=True),
        ),
    ]
