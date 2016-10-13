# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0013_servicioscostos'),
    ]

    operations = [
        migrations.CreateModel(
            name='CostosPorCliente',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('servicio', models.CharField(max_length=100)),
                ('costo', models.DecimalField(max_digits=10, decimal_places=2)),
                ('cliente', models.ForeignKey(blank=True, to='clientes.Cliente', null=True)),
            ],
        ),
        migrations.RenameField(
            model_name='servicioscostos',
            old_name='fisioterapia',
            new_name='pago',
        ),
        migrations.RemoveField(
            model_name='servicioscostos',
            name='cliente',
        ),
        migrations.RemoveField(
            model_name='servicioscostos',
            name='informe_final',
        ),
        migrations.RemoveField(
            model_name='servicioscostos',
            name='medicina_laboral',
        ),
        migrations.RemoveField(
            model_name='servicioscostos',
            name='monto_pago',
        ),
        migrations.RemoveField(
            model_name='servicioscostos',
            name='puesto_trabajo',
        ),
        migrations.RemoveField(
            model_name='servicioscostos',
            name='total',
        ),
        migrations.RemoveField(
            model_name='servicioscostos',
            name='trabajo_social',
        ),
        migrations.AddField(
            model_name='servicioscostos',
            name='costo',
            field=models.DecimalField(default=1, max_digits=10, decimal_places=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='servicioscostos',
            name='servicio',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
