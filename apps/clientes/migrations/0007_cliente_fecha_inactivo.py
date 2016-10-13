# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0006_auto_20160506_2023'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='fecha_inactivo',
            field=models.DateField(null=True, blank=True),
        ),
    ]
