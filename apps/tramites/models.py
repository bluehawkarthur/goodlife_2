from django.db import models


class Tramite(models.Model):
	tipo_tramite = models.CharField(max_length=150)
	observaciones = models.CharField(max_length=500, blank=True)

	def __unicode__(self):
		return self.tipo_tramite


class TramiteAfp(models.Model):
	tipo_afp = models.CharField(max_length=150)
	observaciones = models.CharField(max_length=500, blank=True)

	def __unicode__(self):
		return self.tipo_afp