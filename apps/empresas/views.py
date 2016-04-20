from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponseRedirect 

from .models import Empresa



class RegistarEmpresa(CreateView):
	template_name = 'empresas/registrar_empresa.html'
	model = Empresa
	fields = ('razon_social', 'direccion', 'telefono1', 'telefono2', 'nro_patronal', 'departamento', 'municipios')
	success_url = reverse_lazy('listar_empresa')


class EmpresaList(ListView):
	template_name = 'empresas/lista_empresa.html'
	model = Empresa


class EmpresaDetail(DetailView):
	template_name = 'empresas/detail_empresa.html'
	model = Empresa
	success_url = reverse_lazy('listar_empresa')


class EmpresaUpdateView(UpdateView):
	template_name = 'empresas/update_empresa.html'
	model = Empresa
	fields = ('razon_social', 'direccion', 'telefono1', 'telefono2', 'nro_patronal', 'departamento', 'municipios')
	success_url = reverse_lazy('listar_empresa')


class EmpresaDelete(DeleteView):
    model = Empresa
    success_url = reverse_lazy('listar_empresa')


def eliminar(request, id):
	p = Empresa.objects.get(id=id)
	p.delete()
	return HttpResponseRedirect(reverse_lazy('listar_empresa'))