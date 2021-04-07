from django.urls import path
from . import views

urlpatterns = [
    # home view = sitio raíz
    path('', views.home, name='home'),
    # about view
    path('about/', views.about, name='about'),
]