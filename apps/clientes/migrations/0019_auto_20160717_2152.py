# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0018_costosporcliente_cancelado'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='servicioscobrocliente',
            name='cancelado',
        ),
        migrations.AlterField(
            model_name='servicioscobrocliente',
            name='total',
            field=models.DecimalField(null=True, max_digits=10, decimal_places=2, blank=True),
        ),
    ]
