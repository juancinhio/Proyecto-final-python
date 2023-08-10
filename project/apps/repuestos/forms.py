from django import forms
from .models import Servicio

class BaseMantenimientoForm(forms.Form):
    servicios = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, required=False)

    def __init__(self, categoria_nombre, *args, **kwargs):
        super().__init__(*args, **kwargs)
        servicios = Servicio.objects.filter(categoria__nombre=categoria_nombre)
        servicios_choices = [(servicio.id, servicio.nombre) for servicio in servicios]
        self.fields['servicios'].choices = servicios_choices

class AfinacionForm(BaseMantenimientoForm):
    def __init__(self, *args, **kwargs):
        super().__init__(categoria_nombre='Afinacion', *args, **kwargs)

class FrenosForm(BaseMantenimientoForm):
    def __init__(self, *args, **kwargs):
        super().__init__(categoria_nombre='Frenos', *args, **kwargs)

class SuspensionForm(BaseMantenimientoForm):
    def __init__(self, *args, **kwargs):
        super().__init__(categoria_nombre='Suspensión', *args, **kwargs)

class ServiceForm(BaseMantenimientoForm):
    def __init__(self, *args, **kwargs):
        super().__init__(categoria_nombre='Service', *args, **kwargs)

class EmbragueForm(BaseMantenimientoForm):
    def __init__(self, *args, **kwargs):
        super().__init__(categoria_nombre='Embrague', *args, **kwargs)

class DistribucionForm(BaseMantenimientoForm):
    def __init__(self, *args, **kwargs):
        super().__init__(categoria_nombre='Distribución', *args, **kwargs)

class CircuitoRefrigeranteForm(BaseMantenimientoForm):
    def __init__(self, *args, **kwargs):
        super().__init__(categoria_nombre='Circuito Refrigerante', *args, **kwargs)

class ElectricidadForm(BaseMantenimientoForm):
    def __init__(self, *args, **kwargs):
        super().__init__(categoria_nombre='Electricidad', *args, **kwargs)


class MotorForm(BaseMantenimientoForm):
    def __init__(self, *args, **kwargs):
        super().__init__(categoria_nombre='Motor', *args, **kwargs)

class OtrosForm(BaseMantenimientoForm):
    def __init__(self, *args, **kwargs):
        super().__init__(categoria_nombre='Otros', *args, **kwargs)