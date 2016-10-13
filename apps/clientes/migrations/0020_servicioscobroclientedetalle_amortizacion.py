# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0019_auto_20160717_2152'),
    ]

    operations = [
        migrations.AddField(
            model_name='servicioscobroclientedetalle',
            name='amortizacion',
            field=models.DecimalField(null=True, max_digits=10, decimal_places=2, blank=True),
        ),
    ]
