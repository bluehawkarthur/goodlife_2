from django.shortcuts import render
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponseRedirect 

from .models import Clinica


class RegistrarClinica(CreateView):
	template_name = 'clinicas/registrar_clinica.html'
	model = Clinica
	fields = ('razon_social', 'direccion', 'telefono1', 'telefono2')
	success_url = reverse_lazy('listar_clinica')


class ClinicaList(ListView):
	template_name = "clinicas/lista_clinicas.html"
	model = Clinica


class ClinicaDetail(DetailView):
	template_name = 'clinicas/detail_clinica.html'
	model = Clinica
	success_url = reverse_lazy('listar_clinica')


class ClinicaUpdateView(UpdateView):
	template_name = 'clinicas/update_clinica.html'
	model = Clinica
	fields = ('razon_social', 'direccion', 'telefono1', 'telefono2')
	success_url = reverse_lazy('listar_clinica')


class ClinicaDelete(DeleteView):
    model = Clinica
    success_url = reverse_lazy('listar_clinica')


def eliminar(request, id):
	p = Clinica.objects.get(id=id)
	p.delete()
	return HttpResponseRedirect(reverse_lazy('listar_clinica'))