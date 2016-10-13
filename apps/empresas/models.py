from django.db import models


class Empresa(models.Model):
	razon_social = models.CharField(max_length=150)
	direccion = models.CharField(max_length=150)
	telefono1 = models.CharField(max_length=20, blank=True)
	telefono2 = models.CharField(max_length=20, blank=True)
	nro_patronal = models.CharField(max_length=50, blank=True)
	departamento = models.CharField(max_length=100)
	municipios = models.CharField(max_length=100)

	def __unicode__(self):
		return self.razon_social