# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0016_auto_20160711_1503'),
    ]

    operations = [
        migrations.CreateModel(
            name='ServiciosCobroCliente',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha', models.DateField()),
                ('num_recibo', models.IntegerField()),
                ('total', models.DecimalField(max_digits=10, decimal_places=2)),
                ('cancelado', models.BooleanField(default=False)),
                ('cliente', models.ForeignKey(blank=True, to='clientes.Cliente', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ServiciosCobroClienteDetalle',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('servicio', models.CharField(max_length=100)),
                ('costo', models.DecimalField(max_digits=10, decimal_places=2)),
                ('pago', models.DecimalField(max_digits=10, decimal_places=2)),
                ('cobro', models.ForeignKey(blank=True, to='clientes.ServiciosCobroCliente', null=True)),
            ],
        ),
    ]
