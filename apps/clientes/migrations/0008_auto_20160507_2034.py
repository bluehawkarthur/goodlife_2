# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0007_cliente_fecha_inactivo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='cel_per_referencia',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='persona_referencia',
            field=models.CharField(max_length=150, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='telefono_per_referencia',
            field=models.IntegerField(null=True, blank=True),
        ),
    ]
