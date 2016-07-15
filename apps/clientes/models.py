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
	telefono = models.IntegerField(null=True, blank=True)
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
	seguro = models.CharField(max_length=50, null=True, blank=True)

	def __unicode__(self):
		return "%s-%s-%s" % (self.codigo_gl, self.nombres, self.apellidos)


class DtoCodigo(models.Model):
	departamento = models.CharField(max_length=50, choices=DEP_CHOICES)
	short = models.CharField(max_length=4, null=True, blank=True)
	cantidad = models.IntegerField(default=0)

	def __unicode__(self):
		return "%s - %s" % (self.departamento, self.cantidad)


class ServiciosCostos(models.Model):    # Cobros Default
	servicio = models.CharField(max_length=100, null=True, blank=True)
	costo = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

	def __unicode__(self):
		return "%s - %s" % (self.servicio, self.costo)


class CostosPorCliente(models.Model):
	cliente = models.ForeignKey(Cliente, null=True, blank=True)
	servicio = models.CharField(max_length=100)
	costo = models.DecimalField(max_digits=10, decimal_places=2)
	pago = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
	cancelado = models.BooleanField(default=False)

	def __unicode__(self):
		return "%s - %s -%s" % (self.cliente.codigo_gl, self. servicio, self.costo)


class ServiciosCobroCliente(models.Model): # Cabecera de Cobros
	cliente = models.ForeignKey(Cliente, null=True, blank=True)
	fecha = models.DateField()
	num_recibo = models.IntegerField()
	total = models.DecimalField(max_digits=10, decimal_places=2)
	cancelado = models.BooleanField(default=False)

	def __unicode__(self):
		return "%s - %s" % (self.cliente.codigo_gl, self.fecha)


class ServiciosCobroClienteDetalle(models.Model): # Detalle de Cobros
	cobro = models.ForeignKey(ServiciosCobroCliente, null=True, blank=True)
	servicio = models.CharField(max_length=100)
	costo = models.DecimalField(max_digits=10, decimal_places=2)
	pago = models.DecimalField(max_digits=10, decimal_places=2)

	def __unicode__(self):
		return "%s - %s - %s - %s" % (self.cobro, self.servicio, self.costo, self.pago)