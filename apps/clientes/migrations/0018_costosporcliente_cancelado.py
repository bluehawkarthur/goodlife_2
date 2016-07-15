# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0017_servicioscobrocliente_servicioscobroclientedetalle'),
    ]

    operations = [
        migrations.AddField(
            model_name='costosporcliente',
            name='cancelado',
            field=models.BooleanField(default=False),
        ),
    ]
