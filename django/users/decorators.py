from django.shortcuts import redirect
from django.contrib import messages

# creo decorador para evitar que usuarios logueados accedan al login o a la registración
def unauthenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect("home")
        else:
            return view_func(request, *args, **kwargs)
    return wrapper_func


def allowed_users(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):
            grupo = None
            if request.user.groups.exists():
                grupo = request.user.groups.all()[0].name

            if 'admin' and request.user.is_superuser:
                return view_func(request, *args, **kwargs)
            elif grupo in allowed_roles:
                return view_func(request, *args, **kwargs)
            else:
                messages.warning(request, 'Acceso no autorizado')
                return redirect("home")
        return wrapper_func
    return decorator

