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
	codigo_gl = forms.CharField(label="CODIG")
	ciudad_origen = forms.ChoiceField(label="CIUDAD ORIGEN", choices = DEP_CHOICES)
	nombres = forms.CharField(label="NOMBRES")
	apellidos = forms.CharField(label="APELLIDOS")
	fecha_naciemiento = forms.DateField(label="FECHA DE NACIMIENTO", required=False)
	edad = forms.IntegerField(label="EDAD")
	ci = forms.IntegerField(label="CI")
	expedido = forms.CharField(label="EXPEDIDO")
	telefono = forms.IntegerField(label="TELEFONO", required=False)
	cel = forms.IntegerField(label="CELULAR", required=False)
	foto = forms.ImageField(label="FOTO", required=False)
	activo = forms.BooleanField(label="ACITVO", initial=True, required=False)
	empresa = forms.ModelChoiceField(label="ENPRESA", queryset=Empresa.objects.all())
	tramite = forms.ModelChoiceField(label="TAMITE", queryset=Tramite.objects.all())
	afps = forms.ModelChoiceField(label="AFPS", queryset=TramiteAfp.objects.all())
	clinica = forms.ModelChoiceField(label="CLINICA", queryset=Clinica.objects.all())
	persona_referencia = forms.CharField(label="PERSONA REFERENCIA", required=False)
	telefono_per_referencia = forms.IntegerField(label="TELEFONO PER REFERENCIA", required=False)
	cel_per_referencia = forms.IntegerField(label="CELE_PER_REFERENCIA", required=False)
	fecha_inactivo = forms.DateField(label="FECHA_INACTIVO", required=False)
	seguro = forms.CharField(label="SEGURO", required=False)
	imagenf = forms.CharField(label="IMAGENF", required=False)
	
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
