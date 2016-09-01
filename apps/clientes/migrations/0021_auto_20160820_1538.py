# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0020_servicioscobroclientedetalle_amortizacion'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='expedido',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cliente',
            name='fecha_naciemiento',
            field=models.DateField(null=True, blank=True),
        ),
    ]
