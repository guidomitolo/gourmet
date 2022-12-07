from rest_framework import viewsets
from ..serializers.menu import ProductoSerializer
from menu.models import Producto



class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
