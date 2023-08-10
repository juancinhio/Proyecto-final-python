from django.db import models

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self) -> str:
        return f"{self.nombre}"


class Servicio(models.Model):
    nombre = models.CharField(max_length=100)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    pedidos = models.BooleanField(default=False)
    cantidad = models.IntegerField(default=0)
    ok = models.BooleanField(default=False)
    precio = models.IntegerField(default=0)
    

    def __str__(self) -> str:
        return f"{self.nombre} {self.categoria} {self.pedidos} {self.cantidad} {self.ok}"

    

class Mantenimiento(models.Model):
    servicios = models.ManyToManyField(Servicio)
    precio_total = models.IntegerField(default=0)

    def __str__(self) -> str:
        return f"{self.servicios}"

