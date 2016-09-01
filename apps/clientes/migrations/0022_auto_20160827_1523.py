# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0021_auto_20160820_1538'),
    ]

    operations = [
        migrations.CreateModel(
            name='CarteraCliente',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('examen', models.CharField(max_length=100)),
                ('deuda', models.DecimalField(null=True, max_digits=10, decimal_places=2, blank=True)),
                ('pago', models.DecimalField(null=True, max_digits=10, decimal_places=2, blank=True)),
                ('fecha', models.DateField()),
                ('num_recibo', models.IntegerField()),
            ],
        ),
        migrations.AlterField(
            model_name='cliente',
            name='expedido',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='carteracliente',
            name='cliente',
            field=models.ForeignKey(blank=True, to='clientes.Cliente', null=True),
        ),
    ]
