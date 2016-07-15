from django import forms, http
from django.forms import modelformset_factory
from apps.clientes.models import ServiciosCostos


CostosFormSet = modelformset_factory(ServiciosCostos, extra=0, fields=('servicio', 'costo'))

class CostosForm(CostosFormSet):

    def add_fields(self, form, index):
        super(CostosForm, self).add_fields(form, index)
    