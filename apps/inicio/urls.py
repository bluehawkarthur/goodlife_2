from django.conf.urls import include, url
from .views import Inicio, Main, LoginView, LogoutView, Index

urlpatterns = [

    url(r'^$', Index.as_view(), name='index'),
    url(r'^inicio/$', Inicio.as_view(), name='inicio'),
    #url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'inicio/login.html'}, name='login'),
    #url(r'^salir/$', 'django.contrib.auth.views.logout_then_login', name='logout'),
    url(r'^main/$', Main.as_view(), name='main'),

    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^logout/$', LogoutView.as_view(), name='logout'),
    url(r'^cobros/$', 'apps.inicio.views.cobros', name='cobros'),
    url(r'^buscar_cliente/$', 'apps.inicio.views.searchCliente', name='buscar_cliente'),
    url(r'^registrar_cobro/$', 'apps.inicio.views.addCobro', name='registrar_cobro'),
    url(r'^detallecartera/(?P<pk>\d+)$', 'apps.inicio.views.detalleCartera', name='detallecartera'),

]
