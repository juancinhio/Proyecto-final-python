from django import forms
from cliente.models import Cliente
from vehiculo.models import Vehiculo
from .models import AltaVehiculo

class altaVehiculoForm(forms.ModelForm):
    cliente_nombre = forms.CharField(label='Nombre del Cliente', max_length=50)
    cliente_apellido = forms.CharField(label='Apellido del Cliente', max_length=50)
    cliente_dni = forms.CharField(label='DNI del Cliente', max_length=50)
    cliente_telefono = forms.CharField(label='Teléfono del Cliente', max_length=50)
    cliente_domicilio = forms.CharField(label='domicilio del cliente', max_length=50)
    
    vehiculo_marca = forms.CharField(label='Marca del Vehículo', max_length=50)
    vehiculo_modelo = forms.CharField(label='Modelo del Vehículo', max_length=100)
    vehiculo_patente = forms.CharField(label='patente del Vehículo', max_length=50)
    vehiculo_km = forms.CharField(label='kilometraje del Vehículo', max_length=100)
    
    class Meta:
        model = AltaVehiculo
        fields = ['cliente_nombre', 'cliente_apellido', 'cliente_dni', 'cliente_telefono','cliente_domicilio',
                  'vehiculo_marca', 'vehiculo_modelo', 'vehiculo_patente','vehiculo_km']