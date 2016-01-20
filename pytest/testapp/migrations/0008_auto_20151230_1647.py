# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0007_auto_20151230_0723'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='player',
            name='tgm_chatid',
        ),
        migrations.AddField(
            model_name='player',
            name='tgm_first_name',
            field=models.CharField(max_length=2000, verbose_name=b"Telegram user's first name", blank=True),
        ),
        migrations.AddField(
            model_name='player',
            name='tgm_last_name',
            field=models.CharField(max_length=2000, verbose_name=b"Telegram user's last name", blank=True),
        ),
        migrations.AddField(
            model_name='player',
            name='tgm_user_id',
            field=models.CharField(default=1, max_length=2000, verbose_name=b'Telegram user id'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='player',
            name='tgm_user_name',
            field=models.CharField(max_length=2000, verbose_name=b'Telegram username', blank=True),
        ),
    ]
