# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [('testapp', '0006_auto_20151229_0546'), ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='qtype',
            field=models.CharField(default=b'C',
                                   max_length=10,
                                   verbose_name=b'question type',
                                   choices=[
                                       (b'O', b'open question'), (
                                           b'C', b'close question')
                                   ]), ),
        migrations.AlterField(
            model_name='test',
            name='name',
            field=models.CharField(unique=True,
                                   max_length=200,
                                   verbose_name=b'Test name'), ),
    ]
