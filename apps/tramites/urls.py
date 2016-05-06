from django.conf.urls import include, url
from .views import RegistrarTramite, RegistrarTramiteAfp, TramiteList, TramiteDetail, TramiteUpdate, TramiteAfpList, TramiteAfpDetail, TramiteAfpUpdate


urlpatterns = [
    url(r'^registrar_tramite/$', RegistrarTramite.as_view(), name='registrar_tramite'),
    url(r'^listar_tramite/$', TramiteList.as_view(), name='listar_tramite'),
    url(r'^detail_tramite/(?P<pk>\d+)$', TramiteDetail.as_view(), name='tramite_detail'),
    url(r'^update_tramite/(?P<pk>\d+)$', TramiteUpdate.as_view(), name='tramite_update'),
    url(r'^delete_tramite/(?P<id>\d+)$', 'apps.tramites.views.eliminarTramite', name='tramite_delete'),


    url(r'^registrar_tramiteafp/$', RegistrarTramiteAfp.as_view(), name='registrar_tramiteafp'),
    url(r'^listar_tramiteafp/$', TramiteAfpList.as_view(), name='listar_tramiteafp'),
    url(r'^detail_tramiteafp/(?P<pk>\d+)$', TramiteAfpDetail.as_view(), name='tramiteafp_detail'),
    url(r'^update_tramiteafp/(?P<pk>\d+)$', TramiteAfpUpdate.as_view(), name='tramiteafp_update'),
    url(r'^delete_tramiteafp/(?P<id>\d+)$', 'apps.tramites.views.eliminarTramiteAfp', name='tramiteafp_delete'),

]
