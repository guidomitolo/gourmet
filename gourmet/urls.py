"""gourmet URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

# vistas por defecto en django
from django.contrib.auth import views as auth_views


urlpatterns = [
    # acceso a web administrador
    path('admin/', admin.site.urls),
    # acceso a main
    path('', include('main.urls')),
    # acceso al menu
    path('menu/', include('menu.urls')),
    # acceso a la tienda
    path('tienda/', include('tienda.urls')),
    
    # acceso al registro de usuarios
    # path('register/', include('users.urls')),
    path('users/', include('users.urls')),

    # acceso al logueo de usuarios
    # path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),

    # acceso a la vista de deslogueo
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),

    path('reseteo-pass/',
        auth_views.PasswordResetView.as_view(
            template_name='users/pass/reset.html'
        ),
        name='password_reset'),
    path('reseteo-pass/done/',
         auth_views.PasswordResetDoneView.as_view(
             template_name='users/pass/instructions.html'
         ),
         name='password_reset_done'),
    path('reseteo-pass-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name='users/pass/reset_confirm.html'
         ),
         name='password_reset_confirm'),
    path('reseteo-pass-complete/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name='users/pass/reset_complete.html'
         ),
         name='password_reset_complete'),

] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
