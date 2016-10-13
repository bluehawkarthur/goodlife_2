from django.shortcuts import render
from apps.clientes.models import ServiciosCostos
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse_lazy, reverse
from .forms import CostosForm

def configCostos(request):

  if request.method == "POST":
    formset = CostosForm(request.POST, queryset=ServiciosCostos.objects.all())

    if formset.is_valid():
    	# print formset.deleted_forms
        for form in formset.forms:
        	user = form.save(commit=False)
	        user.save()

        	# pk = form.cleaned_data['id'].pk


        return HttpResponseRedirect(reverse_lazy('config_costos'))


  else:
    formset = CostosForm(queryset=ServiciosCostos.objects.all())


  return render(request, 'config/costos.html', {'formset': formset})


def eliminarCosto(request):
    idCosto = request.GET['id']
    costo = ServiciosCostos.objects.get(id=idCosto)
    costo.delete()

    json_data = {'success': 'se elimino correctamente'}
    print 'esto es json'
    print json_data

    return HttpResponse(json_data, content_type='application/json')
