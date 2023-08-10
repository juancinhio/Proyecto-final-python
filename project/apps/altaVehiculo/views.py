from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from .models import AltaVehiculo, Cliente, Vehiculo
from .forms import altaVehiculoForm
from django.db.models import Q
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
    FormView
)
from django.core.paginator import Paginator, Page


class AltaVehiculoCreate(FormView):
    form_class = altaVehiculoForm
    template_name = 'altaVehiculo/alta_vehiculo_form.html'
    

    def form_valid(self, form):
        # Crear instancia de Cliente
        cliente = Cliente.objects.create(
            nombre=form.cleaned_data['cliente_nombre'],
            apellido=form.cleaned_data['cliente_apellido'],
            dni=form.cleaned_data['cliente_dni'],
            telefono=form.cleaned_data['cliente_telefono'],
            domicilio=form.cleaned_data['cliente_domicilio']
        )

        # Crear instancia de Vehiculo
        vehiculo = Vehiculo.objects.create(
            marca=form.cleaned_data['vehiculo_marca'],
            modelo=form.cleaned_data['vehiculo_modelo'],
            patente=form.cleaned_data['vehiculo_patente'],
            km=form.cleaned_data['vehiculo_km']
        )

        alta_vehiculo = AltaVehiculo.objects.create(
            cliente_id=cliente,
            vehiculo_id=vehiculo,
        )

        success_url = reverse('altaVehiculo:detail_alta', kwargs={'pk': alta_vehiculo.pk})
        return redirect(success_url)
    
class AltaVehiculoDetail(DetailView):   
    model = AltaVehiculo
    template_name = "altaVehiculo/alta_vehiculo_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        alta_vehiculo = self.object
        cliente = alta_vehiculo.cliente_id
        vehiculo = alta_vehiculo.vehiculo_id
        context['cliente'] = cliente
        context['vehiculo'] = vehiculo
        context['cliente_update_url'] = reverse('cliente:update', kwargs={'cliente_id': cliente.id})
        context['vehiculo_update_url'] = reverse('vehiculo:update', kwargs={'vehiculo_id': vehiculo.id})
        return context

class AltaVehiculoList(ListView):
    model=AltaVehiculo
    template_name="altaVehiculo/alta_vehiculo_list.html"
    context_object_name = "object_list"

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return AltaVehiculo.objects.filter(
                Q(cliente_id__nombre__icontains=query) |
                Q(cliente_id__apellido__icontains=query) |
                Q(cliente_id__telefono__icontains=query) |
                Q(vehiculo_id__patente__icontains=query) |
                Q(vehiculo_id__marca__icontains=query) |
                Q(vehiculo_id__modelo__icontains=query)
            )
        return AltaVehiculo.objects.all()
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        paginator = Paginator(context[self.context_object_name], 5)  
        page_number = self.request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        context['object_list'] = page_obj
        return context
    
class AltaVehiculoDelete(DeleteView):
    model = AltaVehiculo
    template_name = "altaVehiculo/alta_vehiculo_delete.html"
    success_url = reverse_lazy('altaVehiculo:list')  
    
   
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)