from django.urls import reverse
from django.shortcuts import redirect
from django.urls import reverse_lazy
from .models import Cliente
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)

# Create your views here.

from . import forms, models


class ClienteList(ListView):
    model = models.Cliente


class ClienteCreate(CreateView):
    model = models.Cliente
    fields = ['nombre', 'apellido','dni','telefono']
    template_name = 'cliente/cliente_form.html'

    def get_success_url(self):
        # Redirige a la vista con el ID del cliente recién creado
        return reverse_lazy('vehiculo:create', kwargs={'cliente_id': self.object.pk})

    

class ClienteDetail(DetailView):
    model = models.Cliente

class ClienteUpdate(UpdateView):
    model = models.Cliente
    form_class = forms.ClienteForm
    template_name = 'cliente/cliente_update.html' 
    success_url = reverse_lazy("altaVehiculo:list")

    def get_object(self, queryset=None):
        cliente_id = self.kwargs.get('cliente_id')
        return Cliente.objects.get(pk=cliente_id)

class ClienteDelete(DeleteView):
    model = models.Cliente
    success_url = reverse_lazy("cliente:cliente_list")
