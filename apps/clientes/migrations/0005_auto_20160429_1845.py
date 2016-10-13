# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0004_auto_20160416_2100'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='activo',
            field=models.BooleanField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cliente',
            name='edad',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cliente',
            name='foto',
            field=models.ImageField(null=True, upload_to=b'clientes', blank=True),
        ),
        migrations.AddField(
            model_name='cliente',
            name='usuario',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='dtocodigo',
            name='short',
            field=models.CharField(max_length=4, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='afps',
            field=models.ForeignKey(blank=True, to='tramites.TramiteAfp', null=True),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='clinica',
            field=models.ForeignKey(blank=True, to='clinicas.Clinica', null=True),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='codigo_gl',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='empresa',
            field=models.ForeignKey(blank=True, to='empresas.Empresa', null=True),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='fecha_ingreso',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='tramite',
            field=models.ForeignKey(blank=True, to='tramites.Tramite', null=True),
        ),
    ]
