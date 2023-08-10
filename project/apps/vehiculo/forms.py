from django import forms

from . import models


class VehiculoForm(forms.ModelForm):
    class Meta:
        model = models.Vehiculo
        fields = "__all__"
