from django.conf.urls import include, url
from .views import RegistarEmpresa, EmpresaList, EmpresaDetail, EmpresaUpdateView, EmpresaDelete

urlpatterns = [
    url(r'^registrar_empresa/$', RegistarEmpresa.as_view(), name='registrar_empresa'),
    url(r'^listar_empresa/$', EmpresaList.as_view(), name='listar_empresa'),
    url(r'^detail_empresa/(?P<pk>\d+)$', EmpresaDetail.as_view(), name='empresa_detail'),
    url(r'^update_empresa/(?P<pk>\d+)$', EmpresaUpdateView.as_view(), name='empresa_update'),
    #url(r'^delete_empresa/(?P<pk>\d+)$', EmpresaDelete.as_view(), name='empresa_delete'),
    url(r'^delete_empresa/(?P<id>\d+)$', 'apps.empresas.views.eliminar', name='empresa_delete'),
]

