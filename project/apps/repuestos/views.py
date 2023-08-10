
from django.urls import reverse_lazy
from django.views.generic import FormView
from .forms import AfinacionForm, CircuitoRefrigeranteForm, EmbragueForm
from .forms import FrenosForm ,DistribucionForm, ElectricidadForm
from .forms import SuspensionForm , ServiceForm, MotorForm, OtrosForm
from .models import Mantenimiento, Servicio

class AfinacionView(FormView):
    form_class = AfinacionForm
    template_name = 'repuestos/afinacion.html'
    categoria_nombre = 'Afinación'
    success_url = reverse_lazy('home:home')


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['servicios_afinacion'] = Servicio.objects.filter(categoria__nombre=self.categoria_nombre)
        print(context['servicios_afinacion'])
        return context

    def form_valid(self, form):
        mantenimiento = Mantenimiento.objects.create()

        for servicio_id in form.cleaned_data.get('servicios'):
            servicio = Servicio.objects.get(id=servicio_id)
            mantenimiento.servicios.add(servicio)
        
        return super().form_valid(form)

class FrenosView(FormView):
    form_class = FrenosForm
    template_name = 'repuestos/frenos.html'
    categoria_nombre = 'Frenos'
    success_url = reverse_lazy('home:home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['servicios_frenos'] = Servicio.objects.filter(categoria__nombre=self.categoria_nombre)
        print(context['servicios_frenos'])
        return context



    def form_valid(self, form):
        mantenimiento = Mantenimiento.objects.create()

        for servicio_id in form.cleaned_data.get('servicios'):
            servicio = Servicio.objects.get(id=servicio_id)
            mantenimiento.servicios.add(servicio)
        
        return super().form_valid(form)

class SuspensionView(FormView):
    form_class = SuspensionForm
    template_name = 'repuestos/suspencion.html'
    categoria_nombre = 'Suspensión'
    success_url = reverse_lazy('home:home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['servicios_suspencion'] = Servicio.objects.filter(categoria__nombre=self.categoria_nombre)
        print(context['servicios_suspencion'])
        return context

    def form_valid(self, form):
        mantenimiento = Mantenimiento.objects.create()

        for servicio_id in form.cleaned_data.get('servicios'):
            servicio = Servicio.objects.get(id=servicio_id)
            mantenimiento.servicios.add(servicio)
        
        return super().form_valid(form)
    

class ServiceView(FormView):
    form_class = ServiceForm
    template_name = 'repuestos/service.html'
    categoria_nombre = 'Service'
    success_url = reverse_lazy('home:home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['servicios_service'] = Servicio.objects.filter(categoria__nombre=self.categoria_nombre)
        print(context['servicios_service'])
        return context

    def form_valid(self, form):
        mantenimiento = Mantenimiento.objects.create()

        for servicio_id in form.cleaned_data.get('servicios'):
            servicio = Servicio.objects.get(id=servicio_id)
            mantenimiento.servicios.add(servicio)
        
        return super().form_valid(form)
    
class EmbragueView(FormView):
    form_class = EmbragueForm
    template_name = 'repuestos/embrague.html'
    categoria_nombre = 'Embrague'
    success_url = reverse_lazy('home:home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['servicios_embrague'] = Servicio.objects.filter(categoria__nombre=self.categoria_nombre)
        print(context['servicios_embrague'])
        return context

    def form_valid(self, form):
        mantenimiento = Mantenimiento.objects.create()

        for servicio_id in form.cleaned_data.get('servicios'):
            servicio = Servicio.objects.get(id=servicio_id)
            mantenimiento.servicios.add(servicio)
        
        return super().form_valid(form)
    
class DistribucionView(FormView):
    form_class = DistribucionForm
    template_name = 'repuestos/distribucion.html'
    categoria_nombre = 'Distribución'
    success_url = reverse_lazy('home:home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['servicios_distribucion'] = Servicio.objects.filter(categoria__nombre=self.categoria_nombre)
        print(context['servicios_distribucion'])
        return context

    def form_valid(self, form):
        mantenimiento = Mantenimiento.objects.create()

        for servicio_id in form.cleaned_data.get('servicios'):
            servicio = Servicio.objects.get(id=servicio_id)
            mantenimiento.servicios.add(servicio)
        
        return super().form_valid(form)
    
class CircuitoView(FormView):
    form_class = CircuitoRefrigeranteForm
    template_name = 'repuestos/circuito_refrigerante.html'
    categoria_nombre = 'Circuito Refrigerante'
    success_url = reverse_lazy('home:home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['servicios_circuito'] = Servicio.objects.filter(categoria__nombre=self.categoria_nombre)
        print(context['servicios_circuito'])
        return context

    def form_valid(self, form):
        mantenimiento = Mantenimiento.objects.create()

        for servicio_id in form.cleaned_data.get('servicios'):
            servicio = Servicio.objects.get(id=servicio_id)
            mantenimiento.servicios.add(servicio)
        
        return super().form_valid(form)
    
class ElectricidadView(FormView):
    form_class = ElectricidadForm
    template_name = 'repuestos/electricidad.html'
    categoria_nombre = 'Electricidad'
    success_url = reverse_lazy('home:home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['servicios_electricidad'] = Servicio.objects.filter(categoria__nombre=self.categoria_nombre)
        print(context['servicios_electricidad'])
        return context

    def form_valid(self, form):
        mantenimiento = Mantenimiento.objects.create()

        for servicio_id in form.cleaned_data.get('servicios'):
            servicio = Servicio.objects.get(id=servicio_id)
            mantenimiento.servicios.add(servicio)
        
        return super().form_valid(form)

class MotorView(FormView):
    form_class = MotorForm
    template_name = 'repuestos/motor.html'
    categoria_nombre = 'Motor'
    success_url = reverse_lazy('home:home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['servicios_motor'] = Servicio.objects.filter(categoria__nombre=self.categoria_nombre)
        print(context['servicios_motor'])
        return context

    def form_valid(self, form):
        mantenimiento = Mantenimiento.objects.create()

        for servicio_id in form.cleaned_data.get('servicios'):
            servicio = Servicio.objects.get(id=servicio_id)
            mantenimiento.servicios.add(servicio)
        
        return super().form_valid(form)
    
class OtrosView(FormView):
    form_class = OtrosForm
    template_name = 'repuestos/otros.html'
    categoria_nombre = 'Otros'
    success_url = reverse_lazy('home:home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['servicios_otros'] = Servicio.objects.filter(categoria__nombre=self.categoria_nombre)
        print(context['servicios_otros'])
        return context

    def form_valid(self, form):
        mantenimiento = Mantenimiento.objects.create()

        for servicio_id in form.cleaned_data.get('servicios'):
            servicio = Servicio.objects.get(id=servicio_id)
            mantenimiento.servicios.add(servicio)
        
        return super().form_valid(form)