from django.conf.urls import include, url


urlpatterns = [
    url(r'^config_costos/$', 'apps.config.views.configCostos', name='config_costos'),
    url(r'^eliminar_costo/$', 'apps.config.views.eliminarCosto', name='eliminar_costo'),
    # url(r'^save_image/(?P<codigo>[\w\-]+)$', 'apps.clientes.views.SaveImage', name='salvar_imagen'),
]
