from django.db import models
from users.models import Cliente
from menu.models import Producto


class Orden(models.Model):
    # SET_NULL no borrar el cliente
    cliente = models.ForeignKey(Cliente, on_delete=models.SET_NULL, blank=True, null=True)
    fecha_orden = models.DateTimeField(auto_now_add=True)
    # Si "completado" es falso, se puede seguir comprando
    completado = models.BooleanField(default=False, null=True, blank=False)
    trans_id = models.CharField(max_length=200, null=True)

    def __str__(self):
        return f"{self.id}"


class OrdenarProducto(models.Model):
    # SET_NULL no borrar el producto
    producto = models.ForeignKey(Producto, on_delete=models.SET_NULL, null=True)
    orden = models.ForeignKey(Orden, on_delete=models.SET_NULL, null=True)
    cantidad = models.IntegerField(default=0, null=True, blank=True)
    # fecha agregada a la orden
    fecha_agregada = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.id}"


class Despacho(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.SET_NULL, blank=True, null=True)
    orden = models.ForeignKey(Orden, on_delete=models.SET_NULL, null=True)
    direccion = models.CharField(max_length=200, null=True)
    ciudad = models.CharField(max_length=200, null=True)
    estado = models.CharField(max_length=200, null=True)
    postal = models.CharField(max_length=200, null=True)
    fecha_agregada = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.direccion}"
    



