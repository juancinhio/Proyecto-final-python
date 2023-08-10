from django.db import models


class Vehiculo(models.Model):
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=100)
    patente= models.CharField(max_length=50, null=True, blank=True)
    km= models.IntegerField(null=True, blank=True)

    def __str__(self):
        """Representa una instancia de la clase como una cadena de texto"""
        return f"{self.marca} {self.modelo} {self.patente} {self.km}"



