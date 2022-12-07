from rest_framework import viewsets
from ..serializers.store import OrdenSerializer, OrdenarProductoSerializer, DespachoSerializer
from store.models import Orden, OrdenarProducto, Despacho



class OrdenViewSet(viewsets.ModelViewSet):
    queryset = Orden.objects.all()
    serializer_class = OrdenSerializer


class OrdenarProductoViewSet(viewsets.ModelViewSet):
    queryset = OrdenarProducto.objects.all()
    serializer_class = OrdenarProductoSerializer


class DespachoViewSet(viewsets.ModelViewSet):
    queryset = Despacho.objects.all()
    serializer_class = DespachoSerializer