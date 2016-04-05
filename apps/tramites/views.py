from django.views.generic import CreateView, ListView, DetailView, UpdateView
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponseRedirect

from .models import Tramite, TramiteAfp


class RegistrarTramite(CreateView):
	template_name = 'tramites/registrar_tramite.html'
	model = Tramite
	fields = ('tipo_tramite', 'observaciones')
	success_url = reverse_lazy('listar_tramite')


class TramiteList(ListView):
	template_name = 'tramites/lista_tramite.html'
	model = Tramite


class TramiteDetail(DetailView):
	template_name = 'tramites/detail_tramite.html'
	model = Tramite
	success_url = reverse_lazy('listar_tramite')


class TramiteUpdate(UpdateView):
	template_name = 'tramites/update_tramite.html'
	model = Tramite
	fields = ('tipo_tramite', 'observaciones')
	success_url = reverse_lazy('listar_tramite')


def eliminarTramite(request, id):
	t = Tramite.objects.get(id=id)
	t.delete()
	return HttpResponseRedirect(reverse_lazy('listar_tramite'))


class RegistrarTramiteAfp(CreateView):
	template_name = 'tramites/registrar_tramiteafp.html'
	model = TramiteAfp
	fields = ('tipo_afp', 'observaciones')
	success_url = reverse_lazy('listar_tramiteafp')


class TramiteAfpList(ListView):
	template_name = 'tramites/listar_tramite_afp.html'
	model = TramiteAfp


class TramiteAfpDetail(DetailView):
	template_name = 'tramites/detail_tramite_afp.html'
	model = TramiteAfp


class TramiteAfpUpdate(UpdateView):
	template_name = 'tramites/update_tramite_afp.html'
	model = TramiteAfp
	fields = ('tipo_afp', 'observaciones')
	success_url = reverse_lazy('listar_tramiteafp')


def eliminarTramiteAfp(request, id):
	a = TramiteAfp.objects.get(id=id)
	a.delete()
	return HttpResponseRedirect(reverse_lazy('listar_tramiteafp'))