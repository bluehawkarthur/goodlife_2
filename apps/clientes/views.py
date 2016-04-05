from django.shortcuts import render
from django.views.generic import CreateView, ListView, DetailView, UpdateView
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponseRedirect

from .models import Cliente


class RegistrarCliente(CreateView):
	template_name = 'clientes/registrar_cliente.html'
	model = Cliente
	fields = ('codigo_gl', 'fecha_ingreso', 'ciudad_origen', 'nombres', 'apellidos', 'ci', 'telefono', 'cel', 'empresa', 'tramite', 'afps', 'clinica', 'persona_referencia', 'telefono_per_referencia', 'cel_per_referencia')
	success_url = reverse_lazy('listar_cliente')


class ClienteList(ListView):
	template_name = 'clientes/lista_cliente.html'
	model = Cliente


class ClienteDetail(DetailView):
	template_name = 'clientes/detail_cliente.html'
	model = Cliente


class ClienteUpdate(UpdateView):
	template_name = 'clientes/update_cliente.html'
	model = Cliente
	fields = ('fecha_ingreso', 'ciudad_origen', 'nombres', 'apellidos', 'ci', 'telefono', 'cel', 'empresa', 'tramite', 'afps', 'clinica', 'persona_referencia', 'telefono_per_referencia', 'cel_per_referencia')
	success_url = reverse_lazy('listar_cliente')


def eliminarCliente(request, id):
	cli = Cliente.objects.get(id=id)
	cli.delete()
	return HttpResponseRedirect(reverse_lazy('listar_cliente'))