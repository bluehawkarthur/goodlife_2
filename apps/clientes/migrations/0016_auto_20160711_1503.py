# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0015_auto_20160708_2028'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicioscostos',
            name='costo',
            field=models.DecimalField(null=True, max_digits=10, decimal_places=2, blank=True),
        ),
        migrations.AlterField(
            model_name='servicioscostos',
            name='servicio',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
    ]
