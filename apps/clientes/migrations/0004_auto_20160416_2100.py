# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0003_dtocodigo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dtocodigo',
            name='cantidad',
            field=models.IntegerField(default=0),
        ),
    ]
