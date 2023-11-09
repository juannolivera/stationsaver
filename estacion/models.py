from django.db import models

class Surtidor(models.Model):
    nombre = models.CharField(max_length=50)
    tipo_combustible = models.CharField(max_length=10)
    precio_por_litro = models.DecimalField(max_digits=5, decimal_places=2)

class Transaccion(models.Model):
    surtidor = models.ForeignKey(Surtidor, on_delete=models.CASCADE)
    cantidad = models.DecimalField(max_digits=5, decimal_places=2)
    fecha = models.DateTimeField(auto_now_add=True)
