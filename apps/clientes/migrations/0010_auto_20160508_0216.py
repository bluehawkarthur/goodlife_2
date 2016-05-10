# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0009_auto_20160507_2036'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='cel',
            field=models.IntegerField(null=True, blank=True),
        ),
    ]
