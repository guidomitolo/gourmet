from django.contrib import admin
from .models import Orden, OrdenarProducto, Despacho

admin.site.register(Orden)
admin.site.register(OrdenarProducto)
admin.site.register(Despacho)
