# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0012_auto_20160513_1550'),
    ]

    operations = [
        migrations.CreateModel(
            name='ServiciosCostos',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('informe_final', models.DecimalField(null=True, max_digits=10, decimal_places=2, blank=True)),
                ('fisioterapia', models.DecimalField(null=True, max_digits=10, decimal_places=2, blank=True)),
                ('medicina_laboral', models.DecimalField(null=True, max_digits=10, decimal_places=2, blank=True)),
                ('puesto_trabajo', models.DecimalField(null=True, max_digits=10, decimal_places=2, blank=True)),
                ('trabajo_social', models.DecimalField(null=True, max_digits=10, decimal_places=2, blank=True)),
                ('monto_pago', models.DecimalField(null=True, max_digits=10, decimal_places=2, blank=True)),
                ('total', models.DecimalField(null=True, max_digits=10, decimal_places=2, blank=True)),
                ('cliente', models.ForeignKey(blank=True, to='clientes.Cliente', null=True)),
            ],
        ),
    ]
