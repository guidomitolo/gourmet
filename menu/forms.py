from django import forms
# import el model
from menu.models import Producto, Categoria

class AgregarCategoria(forms.ModelForm):

    class Meta:
        model = Categoria
        fields = ['nombre', 'slug']


class EliminarCategoria(forms.ModelForm):

    class Meta:
        model = Producto
        fields = ['categoria']

    categoria = forms.ModelMultipleChoiceField(
        queryset=Categoria.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )

    def __init__(self, *args, **kwargs):
        super(EliminarCategoria, self).__init__(*args, **kwargs)


class CargarProducto(forms.ModelForm):

    class Meta:
        model = Producto

        fields = ['categoria', 'nombre', 'detalle', 'celiaco', 'vegano','delivery','ruta_imagen','precio','estado']

        error_messages = {
            'nombre': {
                'required': ("Se debe agregar un nombre de producto"),
                    },
            'precio': {
                'required': ("Se debe definir un precio"),
                },
        }

    categoria = forms.ModelMultipleChoiceField(
        queryset=Categoria.objects.all(),
    )

    def __init__(self, *args, **kwargs):
        super(CargarProducto, self).__init__(*args, **kwargs)


class BuscarProducto(forms.Form):

    querycom = forms.CharField(label='Ingresar el producto',
                widget=forms.TextInput(attrs={'size': 32, 'class': 'form-control'}))