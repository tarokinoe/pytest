# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [('testapp', '0009_auto_20151230_1717'), ]

    operations = [
        migrations.RenameField(model_name='question',
                               old_name='question',
                               new_name='text', ),
    ]
