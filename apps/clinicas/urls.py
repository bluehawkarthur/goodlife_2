from django.conf.urls import include, url
from .views import RegistrarClinica, ClinicaList, ClinicaDetail, ClinicaUpdateView, ClinicaDelete

urlpatterns = [
    url(r'^registrar_clinica/$', RegistrarClinica.as_view(), name='registrar_clinica'),
    url(r'^listar_clinica/$', ClinicaList.as_view(), name='listar_clinica'),
    url(r'^detail_clinica/(?P<pk>\d+)$', ClinicaDetail.as_view(), name='clinica_detail'),
    url(r'^update_clinica/(?P<pk>\d+)$', ClinicaUpdateView.as_view(), name='clinica_update'),
    #url(r'^delete_clinica/(?P<pk>\d+)$', ClinicaDelete.as_view(), name='clinica_delete'),
    url(r'^delete_clinica/(?P<id>\d+)$', 'apps.clinicas.views.eliminar', name='clinica_delete'),
    

]
