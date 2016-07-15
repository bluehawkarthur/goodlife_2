# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0010_auto_20160508_0216'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='seguro',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
    ]
