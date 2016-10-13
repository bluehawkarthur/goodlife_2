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
	fecha_naciemiento = models.DateField(null=True, blank=True)
	edad = models.IntegerField()
	ci = models.BigIntegerField()
	expedido = models.CharField(max_length=100, null=True, blank=True)
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
	total = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

	def __unicode__(self):
		return "%s - %s" % (self.cliente.codigo_gl, self.fecha)


class ServiciosCobroClienteDetalle(models.Model): # Detalle de Cobros
	cobro = models.ForeignKey(ServiciosCobroCliente, null=True, blank=True)
	servicio = models.CharField(max_length=100)
	costo = models.DecimalField(max_digits=10, decimal_places=2)
	pago = models.DecimalField(max_digits=10, decimal_places=2)
	amortizacion = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

	def __unicode__(self):
		return "%s - %s - %s - %s" % (self.cobro, self.servicio, self.costo, self.pago)


class CarteraCliente(models.Model): # Cabecera de Cobros
	cliente = models.ForeignKey(Cliente, null=True, blank=True)
	examen = models.CharField(max_length=100)
	deuda = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
	pago = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
	fecha = models.DateField()
	num_recibo = models.IntegerField(null=True, blank=True)
	
	def __unicode__(self):
		return "%s - %s" % (self.cliente.codigo_gl, self.fecha)


class CarteraCabezera(models.Model): # Cabecera de Cobros
	cliente = models.ForeignKey(Cliente, null=True, blank=True)
	fecha = models.DateField()
	num_recibo = models.IntegerField(null=True, blank=True)
	total = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
	saldo = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
	
	def __unicode__(self):
		return "%s - %s" % (self.cliente.codigo_gl, self.fecha)


class CarteraDetalle(models.Model):
	cartera_c = models.ForeignKey(CarteraCabezera, null=True, blank=True)
	examen = models.CharField(max_length=100)
	deuda = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
	pago = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)


class Documento(models.Model):
	poder = models.BooleanField()
	decl_enf_den_accid = models.BooleanField()
	avc_carnet_aseg = models.BooleanField()
	croquis_domicilio = models.BooleanField()
	cert_nacimiento_aseg = models.BooleanField()
	cert_trabajo = models.BooleanField()
	ci_asegurado = models.BooleanField()
	boleta_trabajo = models.BooleanField()
	cert_matrimonio = models.BooleanField()
	extracto_afp = models.BooleanField()
	cert_d_nacimiento_cony = models.BooleanField()
	actalizacion = models.BooleanField()
	ci_conyugue = models.BooleanField()
	contrato = models.BooleanField()
	cert_nac_hijos = models.BooleanField()
	costo_bs_item_contrato = models.BooleanField()
	ci_hijos = models.BooleanField()
	resolucion_invalidz_hijos = models.BooleanField()
	cliente = models.ForeignKey(Cliente, null=True, blank=True)