# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0024_documento'),
    ]

    operations = [
        migrations.CreateModel(
            name='CarteraCabezera',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha', models.DateField()),
                ('num_recibo', models.IntegerField(null=True, blank=True)),
                ('total', models.DecimalField(null=True, max_digits=10, decimal_places=2, blank=True)),
                ('cliente', models.ForeignKey(blank=True, to='clientes.Cliente', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='CarteraDetalle',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('examen', models.CharField(max_length=100)),
                ('deuda', models.DecimalField(null=True, max_digits=10, decimal_places=2, blank=True)),
                ('pago', models.DecimalField(null=True, max_digits=10, decimal_places=2, blank=True)),
                ('cartera_c', models.ForeignKey(blank=True, to='clientes.CarteraCabezera', null=True)),
            ],
        ),
    ]
