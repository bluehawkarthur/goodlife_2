# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0014_auto_20160708_1445'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='servicioscostos',
            name='pago',
        ),
        migrations.AddField(
            model_name='costosporcliente',
            name='pago',
            field=models.DecimalField(null=True, max_digits=10, decimal_places=2, blank=True),
        ),
    ]
