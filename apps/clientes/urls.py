from django.conf.urls import include, url
from .views import ClienteList, ClienteDetail, ClienteUpdate, SaveImage, practica, ClienteDel

urlpatterns = [
    url(r'^registrar_cliente/$', 'apps.clientes.views.RegistrarCliente', name='registrar_cliente'),
    url(r'^listar_cliente/$', ClienteList.as_view(), name='listar_cliente'),
    url(r'^detail_cliente/(?P<pk>\d+)$', ClienteDetail.as_view(), name='cliente_detail'),
    url(r'^update_cliente/(?P<pk>\d+)$', ClienteUpdate.as_view(), name='cliente_update'),
    url(r'^delete_cliente/(?P<id>\d+)$', 'apps.clientes.views.eliminarCliente', name='cliente_delete'),
    url(r'^registrar_emp/$', 'apps.clientes.views.addEmpresa', name='registrar_empresa'),
    url(r'^registrar_clinic/$', 'apps.clientes.views.addClinica', name='registrar_clinic'),
    url(r'^detalle_cliente/(?P<pk>\d+)$', 'apps.clientes.views.detalleCliente', name='detallecliente'),
    url(r'^save_image/(?P<codigo>[\w\-]+)/$', SaveImage.as_view(), name='salvar_imagen'),
    url(r'^client/', 'apps.clientes.views.client', name="client"),
    url(r'^del/$', ClienteDel.as_view()),
    url(r'^practica/$', practica.as_view(), name='pracica'),
    url(r'^servicios_cliente/(?P<pk>\d+)$', 'apps.clientes.views.serviciosCliente', name="servicios_cliente"),
    url(r'^costos_por_cliente/(?P<pk>\d+)$', 'apps.clientes.views.definir_costos_cliente', name='costos_por_cliente'),
    url(r'^cobro_cliente/(?P<pk>\d+)$', 'apps.clientes.views.cobroCliente', name='cobro_cliente'),
    url(r'^detallecobro/(?P<pk>\d+)$', 'apps.clientes.views.detalleCobro', name='detallecobro'),
    url(r'^reportecobro/(?P<pk>\d+)$', 'apps.clientes.views.reporteCobro', name='reportecobro'),
    # url(r'^save_image/(?P<codigo>[\w\-]+)$', 'apps.clientes.views.SaveImage', name='salvar_imagen'),
]
