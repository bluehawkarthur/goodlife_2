from django.db import models
from apps.empresas.models import Empresa
from apps.tramites.models import Tramite, TramiteAfp
from apps.clinicas.models import Clinica

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

class Cliente(models.Model):
	codigo_gl = models.CharField(max_length=20)
	fecha_ingreso = models.DateField(null=True, blank=True)
	ciudad_origen = models.CharField(max_length=50, choices=DEP_CHOICES)
	nombres = models.CharField(max_length=100)
	apellidos = models.CharField(max_length=100)
	edad = models.IntegerField()
	ci = models.BigIntegerField()
	telefono = models.IntegerField()
	cel = models.IntegerField(null=True, blank=True)
	foto = models.ImageField(upload_to='clientes', null=True, blank=True)
	activo = models.BooleanField(default=True)
	empresa = models.ForeignKey(Empresa, null=True, blank=True)
	tramite = models.ForeignKey(Tramite, null=True, blank=True)
	afps = models.ForeignKey(TramiteAfp, null=True, blank=True)
	clinica = models.ForeignKey(Clinica, null=True, blank=True)
	persona_referencia = models.CharField(max_length=150, null=True, blank=True)
	telefono_per_referencia = models.IntegerField(null=True, blank=True)
	cel_per_referencia = models.IntegerField(null=True, blank=True)
	usuario = models.CharField(max_length=50, null=True, blank=True)
	fecha_inactivo = models.DateField(null=True, blank=True)

	def __unicode__(self):
		return "%s-%s-%s" % (self.codigo_gl, self.nombres, self.apellidos)


class DtoCodigo(models.Model):
	departamento = models.CharField(max_length=50, choices=DEP_CHOICES)
	short = models.CharField(max_length=4, null=True, blank=True)
	cantidad = models.IntegerField(default=0)

	def __unicode__(self):
		return "%s - %s" % (self.departamento, self.cantidad)