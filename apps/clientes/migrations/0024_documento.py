# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0023_auto_20160827_1535'),
    ]

    operations = [
        migrations.CreateModel(
            name='Documento',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('poder', models.BooleanField()),
                ('decl_enf_den_accid', models.BooleanField()),
                ('avc_carnet_aseg', models.BooleanField()),
                ('croquis_domicilio', models.BooleanField()),
                ('cert_nacimiento_aseg', models.BooleanField()),
                ('cert_trabajo', models.BooleanField()),
                ('ci_asegurado', models.BooleanField()),
                ('boleta_trabajo', models.BooleanField()),
                ('cert_matrimonio', models.BooleanField()),
                ('extracto_afp', models.BooleanField()),
                ('cert_d_nacimiento_cony', models.BooleanField()),
                ('actalizacion', models.BooleanField()),
                ('ci_conyugue', models.BooleanField()),
                ('contrato', models.BooleanField()),
                ('cert_nac_hijos', models.BooleanField()),
                ('costo_bs_item_contrato', models.BooleanField()),
                ('ci_hijos', models.BooleanField()),
                ('resolucion_invalidz_hijos', models.BooleanField()),
                ('cliente', models.ForeignKey(blank=True, to='clientes.Cliente', null=True)),
            ],
        ),
    ]
