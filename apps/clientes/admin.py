from django.contrib import admin
from .models import Cliente, DtoCodigo, ServiciosCostos, CostosPorCliente, ServiciosCobroCliente, ServiciosCobroClienteDetalle, CarteraCliente, CarteraDetalle, CarteraCabezera


admin.site.register(Cliente)
admin.site.register(DtoCodigo)
admin.site.register(ServiciosCostos)
admin.site.register(CostosPorCliente)
admin.site.register(ServiciosCobroCliente)
admin.site.register(ServiciosCobroClienteDetalle)
admin.site.register(CarteraCliente)
admin.site.register(CarteraCabezera)
admin.site.register(CarteraDetalle)
