"""goodlife_2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),

    # INICIO
    url(r'^', include('apps.inicio.urls'), name='inicio'),

    # EMPRESAS
    url(r'^', include('apps.empresas.urls'), name='empresas'),

    # CLINICAS
    url(r'^', include('apps.clinicas.urls'), name='clinicas'),

    # CLIENTES
    url(r'^', include('apps.clientes.urls'), name='clientes'),

    # TRAMITES
    url(r'^', include('apps.tramites.urls'), name='tramites'),

    # CONFIGURACION
    url(r'^', include('apps.config.urls'), name='config'),

    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
