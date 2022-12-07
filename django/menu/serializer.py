from .models import Producto, Categoria
from rest_framework import serializers


class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = ['categoria', 'nombre', 'detalle', 'celiaco', 'vegano','delivery','ruta_imagen','precio','estado']

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = "__all__"