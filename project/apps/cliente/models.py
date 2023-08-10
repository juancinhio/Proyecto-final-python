from django.db import models

# Create your models here.

class Cliente(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    dni = models.IntegerField(null=True, blank=True)
    telefono = models.IntegerField(null=True, blank=True)
    domicilio = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.nombre} {self.apellido} {self.dni} {self.telefono}"

