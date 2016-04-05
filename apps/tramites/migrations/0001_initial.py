# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tramite',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tipo_tramite', models.CharField(max_length=150)),
                ('observaciones', models.CharField(max_length=500, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='TramiteAfp',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tipo_afp', models.CharField(max_length=150)),
                ('observaciones', models.CharField(max_length=500, blank=True)),
            ],
        ),
    ]
