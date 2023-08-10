from django.urls import reverse_lazy
from .models import Vehiculo
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)
# Create your views here.

from . import forms, models


class VehiculoList(ListView):
    model = models.Vehiculo


class VehiculoCreate(CreateView):
    model = models.Vehiculo
    fields = ['marca', 'modelo', 'año']
    template_name = 'vehiculo/vehiculo_form.html'
    
    def get_success_url(self):
        # Obtén el ID del vehículo recién creado
        vehiculo_id = self.object.pk
        
        # Obtén el ID del cliente desde los parámetros de la URL
        cliente_id = self.kwargs['cliente_id']
        
        # Redirige a la vista AltaVehiculoCreate con los IDs
        return reverse_lazy('altaVehiculo:create', kwargs={'cliente_id': cliente_id, 'vehiculo_id': vehiculo_id})
    
class VehiculoDetail(DetailView):
    model = models.Vehiculo

class VehiculoUpdate(UpdateView):
    model = models.Vehiculo
    form_class = forms.VehiculoForm
    template_name = "vehiculo/update.html"
    success_url = reverse_lazy("altaVehiculo:list")

    def get_object(self, queryset=None):
        vehiculo_id = self.kwargs.get('vehiculo_id')
        return Vehiculo.objects.get(pk=vehiculo_id)


class VehiculoDelete(DeleteView):
    model = models.Vehiculo
    success_url = reverse_lazy("home:home")
