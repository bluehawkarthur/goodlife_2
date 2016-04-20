# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='ciudad_origen',
            field=models.CharField(max_length=50, choices=[(b'Beni', b'Beni'), (b'Chuquisaca', b'Chuquisaca'), (b'Cochabamba', b'Cochabamba'), (b'La Paz', b'La Paz'), (b'Oruro', b'Oruro'), (b'Pando', b'Pando'), (b'Potosi', b'Potosi'), (b'Santa Cruz', b'Santa Cruz'), (b'Tarija', b'Tarija')]),
        ),
    ]
