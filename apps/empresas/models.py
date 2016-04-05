from django.db import models


class Empresa(models.Model):
	razon_social = models.CharField(max_length=150)
	direccion = models.CharField(max_length=150)
	telefono1 = models.CharField(max_length=20, blank=True)
	telefono2 = models.CharField(max_length=20, blank=True)

	def __unicode__(self):
		return self.razon_social