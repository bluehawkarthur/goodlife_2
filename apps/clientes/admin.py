from django.contrib import admin
from .models import Cliente, DtoCodigo, ServiciosCostos, CostosPorCliente


admin.site.register(Cliente)
admin.site.register(DtoCodigo)
admin.site.register(ServiciosCostos)
admin.site.register(CostosPorCliente)
