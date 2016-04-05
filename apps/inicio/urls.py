from django.conf.urls import include, url
from .views import Inicio, Main, LoginView, LogoutView

urlpatterns = [

    url(r'^$', Inicio.as_view(), name='index'),
    #url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'inicio/login.html'}, name='login'),
    #url(r'^salir/$', 'django.contrib.auth.views.logout_then_login', name='logout'),
    url(r'^main/$', Main.as_view(), name='main'),

    url(r'^login/$', LoginView.as_view(), name='login'),
  	url(r'^logout/$', LogoutView.as_view(), name='logout'),

]
