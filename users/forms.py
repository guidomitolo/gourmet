# modelos
from users.models import Cliente, Empleado, Profile
# modelo de usuario modificado (no por defecto)
from django.contrib.auth import get_user_model
User = get_user_model()
# importar grupo de permisos
from django.contrib.auth.models import Group

# clase para crear los campos
from django import forms
# formulario de Usuario por default en django
from django.contrib.auth.forms import UserCreationForm
# modulo transaction
from django.db import transaction


class RegistroCliente(UserCreationForm):

    # agrego una nueva entrada al formulario por defecto
    first_name = forms.CharField()
    last_name = forms.CharField()
    phone = forms.CharField()
    location = forms.CharField()
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    # sobre-escribir metodo de guardada para agregar campos extras en la db
    @transaction.atomic
    def save(self):
        # commit = false -> override saving
        user = super().save(commit=False)
        # antes de guardar todo, guardo primero los atributos de usuario (genericos)
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        # q tipo de usuario es
        user.is_customer = True
        user.save()
        # guardo los atributos especificos
        cliente = Cliente.objects.create(user=user)
        cliente.phone = self.cleaned_data.get('phone')
        cliente.save()
        return cliente


class RegistroEmpleado(UserCreationForm):

    # agrego una nueva entrada al formulario por defecto
    first_name = forms.CharField()
    last_name = forms.CharField()
    phone = forms.CharField()
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    # sobre-escribir metodo de guardada para agregar campos extras en la db
    @transaction.atomic
    def save(self):
        # commit = false -> override saving
        user = super().save(commit=False)
        # antes de guardar todo, guardo primero los atributos de usuario (genericos)
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        # q tipo de usuario es
        user.is_employee = True
        # inactivo hasta moderación del admin
        user.is_active = False
        # creo el usuario
        user.save()
        # asigno permisos de grupo
        grupo = Group.objects.get(name='empresa')
        user.groups.add(grupo)
        # guardo los atributos especificos
        empleado = Empleado.objects.create(user=user)
        empleado.phone = self.cleaned_data.get('phone')
        empleado.save()
        return empleado


class ActualizarUsuario(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name']


class ActualizarCliente(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['phone', 'location']


class ActualizarEmpleado(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = ['phone']


class ActualizarPerfil(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']