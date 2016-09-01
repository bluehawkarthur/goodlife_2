# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0022_auto_20160827_1523'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carteracliente',
            name='num_recibo',
            field=models.IntegerField(null=True, blank=True),
        ),
    ]
