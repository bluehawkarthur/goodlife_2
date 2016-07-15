from django import forms, http
from .models import Cliente, ServiciosCostos, CostosPorCliente


from django.forms import ModelForm
from django.forms import modelformset_factory

from apps.empresas.models import Empresa
from apps.tramites.models import Tramite, TramiteAfp
from apps.clinicas.models import Clinica


# class ClienteForm(forms.Form):
# 	codigo_gl = forms.CharField(max_length=20)
# 	fecha_ingreso = forms.DateField()
# 	ciudad_origen = forms.CharField()
# 	nombres = forms.CharField(max_length=100)
# 	apellidos = forms.CharField(max_length=100)
# 	edad = forms.IntegerField()
# 	ci = forms.IntegerField()
# 	telefono = forms.IntegerField()
# 	cel = forms.IntegerField()
# 	foto = forms.ImageField()
# 	activo = forms.CharField(max_length=20)
# 	empresa = forms.ModelChoiceField(queryset=Empresa.objects.all())
# 	tramite = forms.ModelChoiceField(queryset=Tramite.objects.all())
# 	afps = forms.ModelChoiceField(queryset=TramiteAfp.objects.all())
# 	clinica = forms.ModelChoiceField(queryset=Clinica.objects.all())
# 	persona_referencia = forms.CharField(max_length=150)
# 	telefono_per_referencia = forms.IntegerField()
# 	cel_per_referencia = forms.IntegerField()
# 	usuario = forms.CharField(max_length=50)

# 	class Meta:
# 		model = Cliente
DEP_CHOICES = (
('Beni', 'Beni'),
('Chuquisaca', 'Chuquisaca'),
('Cochabamba', 'Cochabamba'),
('La Paz', 'La Paz'),
('Oruro', 'Oruro'),
('Pando', 'Pando'),
('Potosi', 'Potosi'),
('Santa Cruz', 'Santa Cruz'),
('Tarija', 'Tarija'),
)

class ClienteForm(forms.Form):
	codigo_gl = forms.CharField()
	ciudad_origen = forms.ChoiceField(choices = DEP_CHOICES)
	nombres = forms.CharField()
	apellidos = forms.CharField()
	edad = forms.IntegerField()
	ci = forms.IntegerField()
	telefono = forms.IntegerField(required=False)
	cel = forms.IntegerField(required=False)
	foto = forms.ImageField(required=False)
	activo = forms.BooleanField(initial=True, required=False)
	empresa = forms.ModelChoiceField(queryset=Empresa.objects.all())
	tramite = forms.ModelChoiceField(queryset=Tramite.objects.all())
	afps = forms.ModelChoiceField(queryset=TramiteAfp.objects.all())
	clinica = forms.ModelChoiceField(queryset=Clinica.objects.all())
	persona_referencia = forms.CharField(required=False)
	telefono_per_referencia = forms.IntegerField(required=False)
	cel_per_referencia = forms.IntegerField(required=False)
	fecha_inactivo = forms.DateField(required=False)
	seguro = forms.CharField(required=False)
	imagenf = forms.CharField(required=False)
	
	# class Meta:
	# 	model = Cliente


CostosFormSet = modelformset_factory(ServiciosCostos, extra=0, fields=('servicio', 'costo'))


class CostosForm(CostosFormSet):

    def add_fields(self, form, index):

        super(CostosForm, self).add_fields(form, index)
        form.fields['servicio'].widget = forms.HiddenInput()


CostosPorClienteFormSet = modelformset_factory(CostosPorCliente, extra=0, fields=('servicio', 'costo', 'pago'))


class CostosPorClienteForm(CostosPorClienteFormSet):

    def add_fields(self, form, index):

        super(CostosPorClienteForm, self).add_fields(form, index)
        form.fields['servicio'].widget = forms.HiddenInput()


CobrosClienteFormSet = modelformset_factory(CostosPorCliente, extra=0, fields=('servicio', 'costo', 'pago'))


class CobrosClienteForm(CobrosClienteFormSet):

    def add_fields(self, form, index):
        super(CobrosClienteForm, self).add_fields(form, index)
        form.fields['servicio'].widget = forms.HiddenInput()
        form.fields['costo'].widget = forms.HiddenInput()
        form.fields['pago'].widget = forms.HiddenInput()
        form.fields['monto'] = forms.IntegerField(required=False)
