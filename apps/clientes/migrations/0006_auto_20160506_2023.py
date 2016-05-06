# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0005_auto_20160429_1845'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='activo',
            field=models.BooleanField(default=True),
        ),
    ]
