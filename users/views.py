from django.shortcuts import render, redirect
# importo formularios
from .forms import RegistroCliente, RegistroEmpleado, ActualizarCliente, ActualizarEmpleado, ActualizarPerfil, ActualizarUsuario
# importo clase para crear vistas-objeto
from django.views.generic import CreateView
# importar clase para emitir mensajes en vistas de clase
from django.contrib.messages.views import SuccessMessageMixin
# importar metodo para emitir mensajes en vistas funcion
from django.contrib import messages
# importo decorador creado ad-hoc
# importor metodo para "decorar" clases
# https://docs.djangoproject.com/en/3.1/topics/class-based-views/intro/#decorating-the-class
from .decorators import unauthenticated_user, allowed_users
from django.utils.decorators import method_decorator
# importar requisito de logueo
from django.contrib.auth.decorators import login_required
# importo modelo de ususario actual para pedir lista de empleados
from django.contrib.auth import get_user_model

User = get_user_model()


@method_decorator(unauthenticated_user, name='dispatch')
class registro_cliente(SuccessMessageMixin, CreateView):
    form_class = RegistroCliente
    template_name = "users/cliente_reg.html"
    success_url = '/'
    success_message = "¡%(first_name)s, ya podés ingresar!"

    def validate(self, form):
        form.save()


@method_decorator(unauthenticated_user, name='dispatch')
class registro_empleado(SuccessMessageMixin, CreateView):
    form_class = RegistroEmpleado
    template_name = "users/empleado_reg.html"
    success_url = '/'
    success_message = "¡%(first_name)s, ya podés ingresar!"

    def validate(self, form):
        form.save()


@login_required
def profile_cliente(request):
    if request.method == 'POST':
        user_form = ActualizarUsuario(
            request.POST, 
            instance=request.user,
        )
        customer_form = ActualizarCliente(
            request.POST, 
            instance=request.user.cliente
        )
        perfil_form = ActualizarPerfil(
            instance=request.user.profile, 
            data=request.POST, 
            files=request.FILES
        )
        if customer_form.is_valid() and perfil_form.is_valid() and user_form.is_valid():
            user_form.save()
            customer_form.save()
            perfil_form.save()
            messages.success(request, f'Has actualizado tus datos')
            return redirect('perfil_cliente')
    else:
        user_form = ActualizarUsuario(instance=request.user)
        customer_form = ActualizarCliente(instance=request.user.cliente)
        perfil_form = ActualizarPerfil(instance=request.user.profile)

    context = {
        'user_form': user_form,
        'customer_form': customer_form,
        'perfil_form': perfil_form
    }

    return render(request, 'users/profile_cliente.html', context)


@login_required
@allowed_users(allowed_roles=['empresa'])
def profile_empleado(request):
    if request.method == 'POST':
        user_form = ActualizarUsuario(
            request.POST, 
            instance=request.user
        )
        employee_form = ActualizarEmpleado(
            request.POST, 
            instance=request.user.empleado
        )
        perfil_form = ActualizarPerfil(
            instance=request.user.profile,
            data=request.POST,
            files=request.FILES
        )
        if user_form.is_valid() and perfil_form.is_valid() and user_form.is_valid():
            user_form.save()
            employee_form.save()
            perfil_form.save()
            messages.success(request, f'Has actualizado tus datos')
            return redirect('perfil_empleado')
    else:
        user_form = ActualizarUsuario(instance=request.user)
        employee_form = ActualizarEmpleado(instance=request.user.empleado)
        perfil_form = ActualizarPerfil(instance=request.user.profile)

    context = {
        'employee_form': employee_form,
        'user_form': user_form,
        'perfil_form': perfil_form
    }

    return render(request, 'users/profile_empleado.html', context)


@login_required
@allowed_users(allowed_roles=['admin'])
def profile_admin(request):
    if request.method == 'POST':
        user_form = ActualizarUsuario(
            request.POST, 
            instance=request.user
        )
        perfil_form = ActualizarPerfil(
            instance=request.user.profile,
            data=request.POST,
            files=request.FILES
        )
        if request.POST.get('actualizar'):
            if user_form.is_valid() and perfil_form.is_valid():
                user_form.save()
                perfil_form.save()
                messages.success(request, f'Has actualizado tus datos')
                return redirect('perfil_admin')
    else:
        user_form = ActualizarUsuario(instance=request.user)
        perfil_form = ActualizarPerfil(instance=request.user.profile)

    context = {
        'user_form': user_form,
        'perfil_form': perfil_form,
    }

    return render(request, 'users/profile_admin.html', context)


@login_required
@allowed_users(allowed_roles=['admin'])
def panel_control(request):
    if request.method == 'POST':
        if request.POST.get('activar'):
            empleado = User.objects.filter(id = request.POST['activar']).first()
            empleado.is_active = True
            empleado.save()
            return redirect('control')
        if request.POST.get('desactivar'):
            empleado = User.objects.filter(id = request.POST['desactivar']).first()
            empleado.is_active = False
            empleado.save()
            return redirect('contrl')
    context = {
        'empleados': User.objects.filter(is_employee = True),
        'total_clientes': User.objects.filter(is_customer = True).count(),
        'total_empleados': User.objects.filter(is_employee = True).count()
    }

    return render(request, 'users/panel_control.html', context)