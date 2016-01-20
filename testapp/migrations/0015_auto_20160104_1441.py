# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations
from django.db import models


class Migration(migrations.Migration):

    dependencies = [('testapp', '0014_test_description'), ]

    operations = [
        migrations.AlterUniqueTogether(name='game',
                                       unique_together=set([]), ),
    ]
