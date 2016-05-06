from django.conf.urls import include, url
from .views import RegistrarCliente, ClienteList, ClienteDetail, ClienteUpdate

urlpatterns = [
    url(r'^registrar_cliente/$', 'apps.clientes.views.RegistrarCliente', name='registrar_cliente'),
    url(r'^listar_cliente/$', ClienteList.as_view(), name='listar_cliente'),
    url(r'^detail_cliente/(?P<pk>\d+)$', ClienteDetail.as_view(), name='cliente_detail'),
    url(r'^update_cliente/(?P<pk>\d+)$', ClienteUpdate.as_view(), name='cliente_update'),
    url(r'^delete_cliente/(?P<id>\d+)$', 'apps.clientes.views.eliminarCliente', name='cliente_delete'),
    url(r'^registrar_emp/$', 'apps.clientes.views.addEmpresa', name='registrar_empresa'),
    

]
