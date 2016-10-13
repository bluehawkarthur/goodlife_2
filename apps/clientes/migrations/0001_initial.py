# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clinicas', '0001_initial'),
        ('tramites', '0001_initial'),
        ('empresas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('codigo_gl', models.IntegerField()),
                ('fecha_ingreso', models.DateField()),
                ('ciudad_origen', models.CharField(max_length=50)),
                ('nombres', models.CharField(max_length=100)),
                ('apellidos', models.CharField(max_length=100)),
                ('ci', models.BigIntegerField()),
                ('telefono', models.IntegerField()),
                ('cel', models.IntegerField()),
                ('persona_referencia', models.CharField(max_length=150)),
                ('telefono_per_referencia', models.IntegerField()),
                ('cel_per_referencia', models.IntegerField()),
                ('afps', models.ForeignKey(to='tramites.TramiteAfp')),
                ('clinica', models.ForeignKey(to='clinicas.Clinica')),
                ('empresa', models.ForeignKey(to='empresas.Empresa')),
                ('tramite', models.ForeignKey(to='tramites.Tramite')),
            ],
        ),
    ]
