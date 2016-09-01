from django.shortcuts import render, HttpResponseRedirect
from django.views.generic import TemplateView, FormView, RedirectView, View
from .forms import LoginForm
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from apps.clientes.models import Cliente, CarteraCliente, CarteraCabezera, CarteraDetalle
from django.http import HttpResponseRedirect, HttpResponseBadRequest, HttpResponse

import json
from django.core.serializers.json import DjangoJSONEncoder


from datetime import date
import datetime
from apps.clientes.htmltopdf import render_to_pdf
from django.conf import settings


class Index(View):

    def get(self, request, *args, **kwargs):

        if not request.user.is_authenticated():
            return HttpResponseRedirect(reverse_lazy('inicio'))
        else:
            return HttpResponseRedirect(reverse_lazy('main'))


class Inicio(TemplateView):
  template_name = 'inicio/index.html'




class Main(TemplateView):
  template_name = 'inicio/main.html'

  @method_decorator(login_required)
  def dispatch(self, *args, **kwargs):
      return super(Main, self).dispatch(*args, **kwargs)



class LoginView(FormView):
    form_class = LoginForm
    template_name = "inicio/login.html"
    success_url = reverse_lazy("main")

    def form_valid(self, form):
        login(self.request, form.get_user())
        return super(LoginView, self).form_valid(form)


class LogoutView(RedirectView):
    pattern_name = 'index'
    success_url = reverse_lazy("index")

    def get(self, request, *args, **kwargs):
        logout(request)
        return super(LogoutView, self).get(request, *args, **kwargs)


def cobros(request):
  return render(request, 'inicio/cobros.html')


def searchCliente(request):
    idCodigo = request.GET.get('codigo_gl', None)

    if idCodigo:
      cliente = Cliente.objects.filter(codigo_gl=idCodigo)
    else:
      nombre_cliente = request.GET['nombre_cliente']
      
      if nombre_cliente:
        cliente = Cliente.objects.filter(nombres__icontains=nombre_cliente)
      else:
        ci_cliente = request.GET['ci_cliente']
        cliente = Cliente.objects.filter(ci=ci_cliente)

    if cliente:
      data = []
      for c in cliente:
          cartera = CarteraCliente.objects.filter(cliente=c.id)
          dcartera = []
          contratodeuda = 0
          contratopago = 0
          fisiodeuda = 0
          fisiopago = 0
          medicinadeuda = 0
          medicinapago = 0
          puestodeuda = 0
          puestopago = 0
          trabajodeuda = 0
          trabajopago = 0

          for car in cartera:
            if car.pago == None:
                car.pago = 0
            if car.examen == 'CONTRATO':
              contratodeuda = contratodeuda + car.deuda
              contratopago = contratopago + car.pago
            if car.examen == 'FISIOTERAPIA':
              fisiodeuda = fisiodeuda + car.deuda
              fisiopago = fisiopago + car.pago
            if car.examen == 'MEDICINA LABORAL':
              medicinadeuda = medicinadeuda + car.deuda
              medicinapago = medicinapago + car.pago
            if car.examen == 'PUESTO DE TRABAJO':
              puestodeuda = puestodeuda + car.deuda
              puestopago = puestopago + car.pago
            if car.examen == 'TRABAJO SOCIAL':
              trabajodeuda = trabajodeuda + car.deuda
              trabajopago = trabajopago + car.pago
          # ============= detalle de cartera ================
          dcartera.append({"examen": "CONTRATO", "deuda": contratodeuda, "pago": contratopago, "saldo": contratodeuda-contratopago})
          dcartera.append({"examen": "FISIOTERAPIA", "deuda": fisiodeuda, "pago": fisiopago, "saldo": fisiodeuda - fisiopago})
          dcartera.append({"examen": "MEDICINA LABORAL", "deuda": medicinadeuda, "pago": medicinapago, "saldo": medicinadeuda - medicinapago})
          dcartera.append({"examen": "PUESTO DE TRABAJO", "deuda": puestodeuda, "pago": puestopago, "saldo": puestodeuda - puestopago})
          dcartera.append({"examen": "TRABAJO SOCIAL", "deuda": trabajodeuda, "pago": trabajopago, "saldo": trabajodeuda - trabajopago})
          # ============= cabezera de cartera ==============
          data.append({"pk": c.id, "codigo_gl": c.codigo_gl, "nombres": c.nombres, "ci": c.ci, "cartera": dcartera})
          
          json_data = json.dumps(data, cls=DjangoJSONEncoder)
          response = HttpResponse(json_data, content_type="application/json")
          response.status_code = 200
          return response
    else:
      response = HttpResponse(content_type="application/json")
      response.status_code = 400
      return response


def addCobro(request):
  if request.method == 'POST':
    print 'llegoooo aaaaquiiii'
    print request.POST['pk_cliente']
    pk = Cliente.objects.get(id=request.POST['pk_cliente'])
    cartera1 = CarteraCliente(cliente=pk, examen='CONTRATO', deuda=0, pago=request.POST['informe_final'], fecha=date.today())
    cartera2 = CarteraCliente(cliente=pk, examen='FISIOTERAPIA', deuda=0, pago=request.POST['fisoterapia'], fecha=date.today())
    cartera3 = CarteraCliente(cliente=pk, examen='MEDICINA LABORAL', deuda=0, pago=request.POST['medicina_laboral'], fecha=date.today())
    cartera4 = CarteraCliente(cliente=pk, examen='PUESTO DE TRABAJO', deuda=0, pago=request.POST['puesto_trabajo'], fecha=date.today())
    cartera5 = CarteraCliente(cliente=pk, examen='TRABAJO SOCIAL', deuda=0, pago=request.POST['trabajo_social'], fecha=date.today())
    cartera_list = [cartera1, cartera2, cartera3, cartera4, cartera5]

    for cartera in cartera_list:
      cartera.save()

    carteracli = CarteraCabezera.objects.exclude(num_recibo__isnull=True).last()
    if carteracli:
        nro = carteracli.num_recibo
        if nro is None:
            nro = 0
    else:
        nro = 0
    
    cabezera = CarteraCabezera(
      cliente=pk,
      fecha=date.today(),
      num_recibo=nro + 1,
      total=request.POST['totales']
    )
    cabezera.save()

    carterac1 = CarteraDetalle(cartera_c=cabezera, examen='CONTRATO', deuda=0, pago=request.POST['informe_final'])
    carterac2 = CarteraDetalle(cartera_c=cabezera, examen='FISIOTERAPIA', deuda=0, pago=request.POST['fisoterapia'])
    carterac3 = CarteraDetalle(cartera_c=cabezera, examen='MEDICINA LABORAL', deuda=0, pago=request.POST['medicina_laboral'])
    carterac4 = CarteraDetalle(cartera_c=cabezera, examen='PUESTO DE TRABAJO', deuda=0, pago=request.POST['puesto_trabajo'])
    carterac5 = CarteraDetalle(cartera_c=cabezera, examen='TRABAJO SOCIAL', deuda=0, pago=request.POST['trabajo_social'])
    carterac_list = [carterac1, carterac2, carterac3, carterac4, carterac5]

    for carterac in carterac_list:
      carterac.save()

    # data = {'pk': clinica.pk, 'razon_socialclinica': clinica.razon_social}
    data = {'pk': cabezera.pk}
    print 'guardoooooooo'
    return HttpResponse(json.dumps(data), content_type='application/json')


def detalleCartera(request, pk):
    cabezera = CarteraCabezera.objects.get(pk=pk)
    detalle = CarteraDetalle.objects.filter(cartera_c=cabezera)

    vd = []
    pago = 0
    costo = 0
    # for d in detalle:
    #     pago = pago + d.pago
    #     costo = costo + d.costo
    #     vd.append(d)
    logo =  settings.MEDIA_ROOT + '/FTG.png'

    data = {
        'logo': logo,
        'cliente': cabezera.cliente,
        'fecha': cabezera.fecha,
        'num_recibo': cabezera.num_recibo,
        'total': cabezera.total,
        'detalle': detalle

    }

    return render_to_pdf('inicio/recibo.html', data)
