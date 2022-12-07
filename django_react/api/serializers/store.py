from rest_framework import serializers
from store.models import Orden, OrdenarProducto, Despacho



class OrdenSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Orden
        fields = "__all__"


class OrdenarProductoSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = OrdenarProducto
        fields = "__all__"


class DespachoSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Despacho
        fields = "__all__"