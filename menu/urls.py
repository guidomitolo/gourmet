from django.urls import path
from . import views

from django.conf.urls import url, include

from rest_framework import routers
from .viewsets import ProductoViewSet, CategoriaViewSet

router = routers.SimpleRouter()
router.register("producto", ProductoViewSet)
router.register("categoria", CategoriaViewSet)

urlpatterns = [ 
    url('', include(router.urls)),
    path('producto', ProductoViewSet.as_view({'get':'list'}), name='api_prod'),
    path('categoria', ProductoViewSet.as_view({'get':'list'}), name='api_cat'),

    # home view = sitio raíz
    path('', views.menu, name='menu'),
    path('cargar', views.cargar_carta, name='cargar'),
    path('<int:item_id>/modificar/', views.modificar, name='modificar'),

    # vista de la busqueda con AJAX
    path('buscar/', views.BuscarProducto.as_view(), name='buscar'),
]