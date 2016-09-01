# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0025_carteracabezera_carteradetalle'),
    ]

    operations = [
        migrations.AddField(
            model_name='carteracabezera',
            name='saldo',
            field=models.DecimalField(null=True, max_digits=10, decimal_places=2, blank=True),
        ),
    ]
