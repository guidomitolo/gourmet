# modelos
from django.contrib.auth import models
from users.models import Cliente, Empleado, Profile
# modelo de usuario modificado (no por defecto)
from django.contrib.auth import get_user_model
User = get_user_model()
# importar grupo de permisos
from django.contrib.auth.models import Group, Permission

# clase para crear los campos
from django import forms
# formulario de Usuario por default en django
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
# modulo transaction
from django.db import transaction

class LoginForm(AuthenticationForm):

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password'].widget.attrs['class'] = 'form-control'

class RegistroCliente(UserCreationForm):

    first_name = forms.CharField(widget = forms.TextInput(
            attrs = {
                'class': 'form-control',
            }
        )
    )
    last_name = forms.CharField(widget = forms.TextInput(
            attrs = {
                'class': 'form-control',
            }
        )
    )
    password1 = forms.CharField(label = 'Contraseña',widget = forms.PasswordInput(
            attrs = {
                'class': 'form-control',
            }
        )
    )
    password2 = forms.CharField(label = 'Contraseña de Confirmación', widget = forms.PasswordInput(
            attrs={
                'class': 'form-control',
            }
        )
    )

    class Meta:
        model = User
        fields = ['username', 'email']
        widgets = {
            'email': forms.TextInput(
                attrs = {
                    "class": "form-control"
                }
            ),
            'username': forms.TextInput(
                attrs = {
                    "class": "form-control"
                }
            ),
        }

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
    first_name = forms.CharField(widget = forms.TextInput(
            attrs = {
                'class': 'form-control',
            }
        )
    )
    last_name = forms.CharField(widget = forms.TextInput(
            attrs = {
                'class': 'form-control',
            }
        )
    )
    password1 = forms.CharField(label = 'Contraseña',widget = forms.PasswordInput(
            attrs = {
                'class': 'form-control',
            }
        )
    )
    password2 = forms.CharField(label = 'Contraseña de Confirmación', widget = forms.PasswordInput(
            attrs={
                'class': 'form-control',
            }
        )
    )

    class Meta:
        model = User
        fields = ['username', 'email']
        widgets = {
            'email': forms.TextInput(
                attrs = {
                    "class": "form-control"
                }
            ),
            'username': forms.TextInput(
                attrs = {
                    "class": "form-control"
                }
            ),
        }

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
        empresa, created = Group.objects.get_or_create(name='empresa')

        permisos = [
                "Can add consulta",
                "Can change consulta",
                "Can delete consulta",
                "Can view consulta",
                "Can add respuesta",
                "Can change respuesta",
                "Can delete respuesta",
                "Can view respuesta",
                "Can add categoria",
                "Can change categoria",
                "Can delete categoria",
                "Can view categoria",
                "Can add producto",
                "Can change producto",
                "Can delete producto",
                "Can view producto"
        ]

        for permiso in permisos:
            empresa.permissions.add(
                Permission.objects.filter(name=permiso).first()
            )

        user.groups.add(empresa)

        empleado = Empleado.objects.create(user=user)
        empleado.save()

        return empleado


class ActualizarUsuario(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username' ,'email', 'first_name', 'last_name']
        widgets = {
            'username': forms.TextInput(
                attrs = {
                    "class": "form-control",
                    "placeholder": "username"
                }
            ),
            'email': forms.TextInput(
                attrs = {
                    "class": "form-control",
                    "placeholder": "Correo"
                }
            ),
            'first_name': forms.TextInput(
                attrs = {
                    "class": "form-control",
                    "placeholder": "Nombre"
                }
            ),
            'last_name': forms.TextInput(
                attrs = {
                    "class": "form-control",
                    "placeholder": "Apellido"
                }
            ),
        }


class ActualizarCliente(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['telefono','calle','altura','localidad','municipio']
        widgets = {
            'telefono': forms.TextInput(
                attrs = {
                    "class": "form-control",
                    "name": "telefono",
                    "placeholder": "Telefono"
                }
            ),
            'calle': forms.TextInput(
                attrs = {
                    "class": "form-control",
                    "name": "calle",
                    "placeholder": "Calle"
                }
            ),
            'altura': forms.TextInput(
                attrs = {
                    "class": "form-control",
                    "name": "altura",
                    "placeholder": "Altura"
                }
            ),
            'localidad': forms.TextInput(
                attrs = {
                    "class": "form-control",
                    "name": "localidad",
                    "placeholder": "Localidad"
                }
            ),
            'municipio': forms.TextInput(
                attrs = {
                    "class": "form-control",
                    "name": "municipio",
                    "placeholder": "Municipio"
                }
            ),
        }


class ActualizarEmpleado(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = ['telefono']
        widgets = {
            'telefono': forms.TextInput(
                attrs = {
                    "class": "form-control"
                }
            )
        }


class ActualizarPerfil(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']