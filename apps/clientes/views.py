from django.shortcuts import render, render_to_response
from django.views.generic import CreateView, ListView, DetailView, UpdateView, TemplateView
from django.core.urlresolvers import reverse_lazy, reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from .models import Cliente, DtoCodigo, ServiciosCostos, CostosPorCliente
from apps.empresas.models import Empresa
from apps.clinicas.models import Clinica
from .forms import ClienteForm, CostosForm, CostosPorClienteForm, CobrosClienteForm
import json

from datetime import date
from django.db.models import Q
import operator
from pure_pagination.mixins import PaginationMixin
from htmltopdf import render_to_pdf
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
import base64
import json
from django.core import serializers
from django.core.exceptions import ObjectDoesNotExist
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
import decimal


# personalize de configuracions de cliente y ciente campos
@method_decorator(csrf_exempt)
def client(request):
  #   config = Cliente.objects.all()
  #   data = serializers.serialize(
  #       'json', config, fields=('codigo_gl', 'fecha_ingreso','ciudad_origen', 'nombres',
  # 'apellidos', 'edad', 'ci', 'telefono', 'cel', 'foto'))
  #   return HttpResponse(data, content_type="application/json")

    data = {"Message": None,
              "Result": "OK",
              "Records": list(),
              "TotalRecordCount": None}
    try:
        start = int(request.GET['jtStartIndex'])
        end = start + int(request.GET['jtPageSize'])
        item_sort = request.GET['jtSorting'].split()[0]
        if request.GET['jtSorting'].split()[1] == 'DESC':
            item_sort = '-' + item_sort
        data['TotalRecordCount'] = Cliente.objects.count()
        for node in Cliente.objects.all().order_by(item_sort)[start:end]:
            data["Records"].append({
                'id': node.pk,
                'codigo_gl': node.codigo_gl,
                'nombres': node.nombres
            })
    except ObjectDoesNotExist:
        data = {"Message": "Error: Node records not found.",
                "Result": "ERROR"}
    return HttpResponse(json.dumps(data), content_type='application/json')


class ClienteDel(TemplateView):
    @method_decorator(csrf_exempt)
    def dispatch(self, request):
        if request.method == "POST":
            n = Cliente.objects.get(id=request.POST['id'])
            if not n:
                data = {"Result": "ERROR",
                        "Message": "Error: Object Does Not Exist"}
            else:
                n.delete()
                data = {"Result": "OK"}
        else:
            data = {"Message": "Error: POST method is required.",
                    "Result": "ERROR"}
        return HttpResponse(json.dumps(data), content_type='application/json')


class practica(TemplateView):
  template_name = 'clientes/pract.html'


def RegistrarCliente(request):
  departamento = 'Cochabamba'
  dep = DtoCodigo.objects.get(departamento=departamento)
  codigo_dep = dep.short + str(dep.cantidad + 1)

  if request.method == 'POST':
    form = ClienteForm(request.POST, request.FILES)
    if form.is_valid():
      print 'entroooooo es validoo jejeje'
      print form.cleaned_data['foto']

      if form.cleaned_data['foto']:
      	foto1 = form.cleaned_data['foto']
      else:
      	if form.cleaned_data['imagenf']:
      		foto1 = 'clientes/'+ form.cleaned_data['codigo_gl'] + ".jpg"
      		fotoname = form.cleaned_data['codigo_gl'] + ".jpg"
      		imagen = base64.b64decode(form.cleaned_data['imagenf'])
      		f = open(settings.MEDIA_ROOT + '/clientes/'+ fotoname, 'wb')
      		f.write(imagen)
      		f.close()
      	else:
      			foto1 = foto1 = form.cleaned_data['foto']

      cliente = Cliente(
        codigo_gl=form.cleaned_data['codigo_gl'],
        fecha_ingreso=date.today(),
        ciudad_origen=form.cleaned_data['ciudad_origen'],
        nombres=form.cleaned_data['nombres'],
        apellidos=form.cleaned_data['apellidos'],
        edad=form.cleaned_data['edad'],
        ci=form.cleaned_data['ci'],
        telefono=form.cleaned_data['telefono'],
        cel=form.cleaned_data['cel'],
        foto=foto1,
        activo=form.cleaned_data['activo'],
        empresa=form.cleaned_data['empresa'],
        tramite=form.cleaned_data['tramite'],
        afps=form.cleaned_data['afps'],
        clinica=form.cleaned_data['clinica'],
        persona_referencia=form.cleaned_data['persona_referencia'],
        telefono_per_referencia=form.cleaned_data['telefono_per_referencia'],
        cel_per_referencia=form.cleaned_data['cel_per_referencia'],
        fecha_inactivo=form.cleaned_data['fecha_inactivo'])
      cliente.save()

      codigod = DtoCodigo.objects.filter(id=dep.pk)
      codigod.update(cantidad=codigod[0].cantidad + 1)

      return HttpResponseRedirect(reverse('detallecliente', args=(cliente.pk,)))

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
    'cel_per_referencia', 'fecha_inactivo')
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

def addClinica(request):
  if request.method == 'POST':
    print 'llegoooo aaaaquiiii'
    print request.POST['telefono1']
    clinica = Clinica(
      razon_social=request.POST['razon_social'],
      direccion=request.POST['direccion'],
      telefono1=request.POST['telefono1'],
      telefono2=request.POST['telefono2'])
    clinica.save()
    data = {'pk': clinica.pk, 'razon_socialclinica': clinica.razon_social}
    print 'guardoooooooo'
    return HttpResponse(json.dumps(data), content_type='application/json')


def detalleCliente(request, pk):
    detalle = Cliente.objects.get(id=pk)

    return render_to_pdf('clientes/clientepdf.html', {'detalle': detalle})


@method_decorator(csrf_exempt)
def serviciosCliente(request, pk):
    cliente = Cliente.objects.get(id=pk)
    costos = ServiciosCostos.objects.filter(cliente=pk)
    if request.method == 'POST':
      print 'llegoooo aaaaquiiii'
      if costos:
        costos.update(informe_final=request.POST['informe_final'],
          fisioterapia=request.POST['fisioterapia'],
          medicina_laboral=request.POST['medicina_laboral'],
          puesto_trabajo=request.POST['puesto_trabajo'],
          trabajo_social=request.POST['trabajo_social'])
      else:
        servicios = ServiciosCostos(
          cliente=cliente,
          informe_final=request.POST['informe_final'],
          fisioterapia=request.POST['fisioterapia'],
          medicina_laboral=request.POST['medicina_laboral'],
          puesto_trabajo=request.POST['puesto_trabajo'],
          trabajo_social=request.POST['trabajo_social'])
        servicios.save()

    # data = {'pk': empresa.pk, 'razon_socialemp': empresa.razon_social}

    return render_to_response('clientes/servicios_cliente.html', {'costos': costos[0]})

# @csrf_exempt
# def SaveImage(request, codigo):
#     print codigo
#     print 'entrooo a save'

#     return HttpResponse('http://localhost:8080/site_media/webcamimages/someimage.jpg')



class SaveImage(TemplateView):

  @csrf_exempt
  def dispatch(self, *args, **kwargs):
		self.filename = self.kwargs['codigo']+'.jpg'
		return super(SaveImage, self).dispatch(*args, **kwargs)

  def post(self, request, *args, **kwargs):

		imagen = base64.b64decode('')
		# save it somewhere
		f = open(settings.MEDIA_ROOT + '/clientes/'+ self.filename, 'wb')
		f.write(imagen)
		f.close()
		# return the URL
		return HttpResponse("/media/clientes/" + self.filename)

  def get(self, request, *args, **kwargs):
		return HttpResponse('No esta pasando el POST')


def definir_costos_cliente(request, pk):

  costocliente = CostosPorCliente.objects.filter(cliente=pk)

  if request.method == "POST":
    if 'nuevo' in request.POST:
      CostosPorCliente.objects.filter(cliente=pk).delete()
      formset = CostosForm(queryset=ServiciosCostos.objects.all())

      return render(request, 'clientes/cobros_por_cliente.html', {'formset': formset, 'cancelado': False})

    if 'guardar' in request.POST:
      if costocliente:
        print 'leeeeeeee'

        formset = CostosPorClienteForm(request.POST, queryset=CostosPorCliente.objects.filter(cliente=pk))
      else:
        formset = CostosForm(request.POST, queryset=ServiciosCostos.objects.all())

      if formset.is_valid():
          for form in formset.forms:
            if costocliente:
              user = form.save(commit=False)
              user.save()
              # costocliente.update(costo=form.cleaned_data['costo'])
            else:
              costo = CostosPorCliente()
              costo.servicio = form.cleaned_data['servicio']
              costo.cliente = Cliente.objects.get(pk=pk)
              costo.costo = form.cleaned_data['costo']
              costo.save()

          return HttpResponseRedirect(reverse_lazy('listar_cliente'))
      else:
        print formset



  else:
    cancelado = False
    contador_pago = 0
    contador = 0
    for d in costocliente:
      contador = contador + 1
      if d.costo == d.pago:
        contador_pago = contador_pago + 1

    if contador == contador_pago:
      cancelado = True

    if costocliente:
      formset = CostosPorClienteForm(queryset=CostosPorCliente.objects.filter(cliente=pk))
    else:
      formset = CostosForm(queryset=ServiciosCostos.objects.all())


  return render(request, 'clientes/cobros_por_cliente.html', {'formset': formset, 'cancelado': cancelado})


def cobroCliente(request, pk):

  if request.method == "POST":

    formset = CobrosClienteForm(request.POST, queryset=CostosPorCliente.objects.filter(cliente=pk))

    if formset.is_valid():
        for form in formset.forms:
            monto = form.cleaned_data['monto']
            pago = form.cleaned_data['pago']
            if pago is None:
              pago = 0

            if monto is None:
              monto = 0

            total_pago = decimal.Decimal(pago) + monto
            user = form.save(commit=False)
            user.pago = total_pago
            user.save()
            # costo = CostosPorCliente()
            # costo.servicio = form.cleaned_data['servicio']
            # costo.cliente = Cliente.objects.get(pk=pk)
            # costo.costo = form.cleaned_data['costo']
            # costo.save()

        return HttpResponseRedirect(reverse_lazy('listar_cliente'))
    else:
      print formset


  else:
    cancelado = False
    datos = CostosPorCliente.objects.filter(cliente=pk)
    contador_pago = 0
    contador = 0
    for d in datos:
      contador = contador + 1
      if d.costo == d.pago:
        contador_pago = contador_pago + 1

    if contador == contador_pago:
      cancelado = True


    formset = CobrosClienteForm(queryset=CostosPorCliente.objects.filter(cliente=pk))


  return render(request, 'clientes/cobro_cliente.html', {'formset': formset, 'cancelado': cancelado})
