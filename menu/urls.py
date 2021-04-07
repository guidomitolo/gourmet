from django.urls import path
from . import views

urlpatterns = [
    # home view = sitio raíz
    path('', views.menu, name='menu'),
    path('cargar', views.cargar_carta, name='cargar'),
    path('<int:item_id>/modificar/', views.modificar, name='modificar'),
]