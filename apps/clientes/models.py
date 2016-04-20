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
	codigo_gl = models.IntegerField()
	fecha_ingreso = models.DateField()
	ciudad_origen = models.CharField(max_length=50, choices=DEP_CHOICES)
	nombres = models.CharField(max_length=100)
	apellidos = models.CharField(max_length=100)
	ci = models.BigIntegerField()
	telefono = models.IntegerField()
	cel = models.IntegerField()
	empresa = models.ForeignKey(Empresa)
	tramite = models.ForeignKey(Tramite)
	afps = models.ForeignKey(TramiteAfp)
	clinica = models.ForeignKey(Clinica)
	persona_referencia = models.CharField(max_length=150)
	telefono_per_referencia = models.IntegerField()
	cel_per_referencia = models.IntegerField()

	def __unicode__(self):
		return "%s-%s-%s" % (self.codigo_gl, self.nombres, self.apellidos)


class DtoCodigo(models.Model):
	departamento = models.CharField(max_length=50, choices=DEP_CHOICES)
	cantidad = models.IntegerField(default=0)

	def __unicode__(self):
		return "%s - %s" % (self.departamento, self.cantidad)