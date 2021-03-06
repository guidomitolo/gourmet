from django.urls import path
from . import views

urlpatterns = [
    path('login', views.login_form, name='login'),

    path('reg_cliente', views.registro_cliente.as_view(), name='cliente_reg'),
    path('reg_empleado', views.registro_empleado.as_view(), name='empleado_reg'),

    path('perfil_cliente', views.profile_cliente, name='perfil_cliente'),
    path('perfil_empleado', views.profile_empleado, name='perfil_empleado'),
    path('perfil_admin', views.profile_admin, name='perfil_admin'),
    path('panel_control', views.panel_control, name='control')
]