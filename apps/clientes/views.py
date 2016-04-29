from django.shortcuts import render, render_to_response
from django.views.generic import CreateView, ListView, DetailView, UpdateView
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from .models import Cliente, DtoCodigo
from apps.empresas.models import Empresa
from .forms import ClienteForm
import json

from datetime import date


def RegistrarCliente(request):
	departamento = 'Cochabamba'
  	dep = DtoCodigo.objects.get(departamento=departamento)
  	codigo_dep = dep.short + str(dep.cantidad + 1)

	if request.method == 'POST':
		form = ClienteForm(request.POST)
		if form.is_valid():
			print 'entroooooo es validoo jejeje'
			cliente = Cliente(
				codigo_gl = form.cleaned_data['codigo_gl'],
				fecha_ingreso = date.today(),
				ciudad_origen = form.cleaned_data['ciudad_origen'],
				nombres = form.cleaned_data['nombres'],
				apellidos = form.cleaned_data['apellidos'],
				edad = form.cleaned_data['edad'],
				ci = form.cleaned_data['ci'],
				telefono = form.cleaned_data['telefono'],
				cel = form.cleaned_data['cel'],
				foto = form.cleaned_data['foto'],
				activo = form.cleaned_data['activo'],
				empresa = form.cleaned_data['empresa'],
				tramite = form.cleaned_data['tramite'],
				afps = form.cleaned_data['afps'],
				clinica = form.cleaned_data['clinica'],
				persona_referencia = form.cleaned_data['persona_referencia'],
				telefono_per_referencia = form.cleaned_data['telefono_per_referencia'],
				cel_per_referencia = form.cleaned_data['cel_per_referencia'],
				usuario = form.cleaned_data['usuario'])
			cliente.save()

			codigod = DtoCodigo.objects.filter(id=dep.pk)
			codigod.update(cantidad=codigod[0].cantidad + 1)

			return HttpResponseRedirect(reverse_lazy('listar_cliente'))
			# return render_to_response('config/crearSucursal.html')
	else:
		print 'entro normalaaaaaaaa'
		
		form = ClienteForm()
	variables = RequestContext(request, {'form': form, 'codigo_dep': codigo_dep})
	return render_to_response('clientes/registrar_cliente.html', variables)


class ClienteList(ListView):
  template_name = 'clientes/lista_cliente.html'
  model = Cliente


class ClienteDetail(DetailView):
  template_name = 'clientes/detail_cliente.html'
  model = Cliente


class ClienteUpdate(UpdateView):
  template_name = 'clientes/update_cliente.html'
  model = Cliente
  fields = ('codigo_gl', 'fecha_ingreso', 'ciudad_origen', 'nombres', 'apellidos', 'edad', 'ci', 'telefono', 'cel',
    'foto', 'activo', 'empresa', 'tramite', 'afps', 'clinica', 'persona_referencia', 'telefono_per_referencia',
    'cel_per_referencia', 'usuario')
  success_url = reverse_lazy('listar_cliente')


def eliminarCliente(request, id):
  cli = Cliente.objects.get(id=id)
  cli.delete()
  return HttpResponseRedirect(reverse_lazy('listar_cliente'))


def addEmpresa(request):

  if request.method == 'POST':
    print 'llegoooo aaaaquiiii'
    print request.POST['telefono1']
    empresa = Empresa(
      razon_social=request.POST['razon_social'],
      direccion=request.POST['direccion'],
      telefono1=request.POST['telefono1'],
      telefono2=request.POST['telefono2'],
      nro_patronal=request.POST['nro_patronal'],
      departamento=request.POST['departamento'],
      municipios=request.POST['municipios'])
    empresa.save()
    data = {'pk': empresa.pk, 'razon_socialemp': empresa.razon_social}
    print 'guardoooooooo'
    return HttpResponse(json.dumps(data), content_type='application/json')
