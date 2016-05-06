# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0002_auto_20160416_2021'),
    ]

    operations = [
        migrations.CreateModel(
            name='DtoCodigo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('departamento', models.CharField(max_length=50, choices=[(b'Beni', b'Beni'), (b'Chuquisaca', b'Chuquisaca'), (b'Cochabamba', b'Cochabamba'), (b'La Paz', b'La Paz'), (b'Oruro', b'Oruro'), (b'Pando', b'Pando'), (b'Potosi', b'Potosi'), (b'Santa Cruz', b'Santa Cruz'), (b'Tarija', b'Tarija')])),
                ('cantidad', models.IntegerField()),
            ],
        ),
    ]
