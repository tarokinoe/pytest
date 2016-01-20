# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0008_auto_20151230_1647'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='tgm_user_id',
            field=models.CharField(unique=True, max_length=2000, verbose_name=b'Telegram user id'),
        ),
    ]
