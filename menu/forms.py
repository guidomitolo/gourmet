from django import forms
# import el model
from menu.models import Producto, Categoria

class AgregarCategoria(forms.ModelForm):

    class Meta:
        model = Categoria
        fields = ['nombre', 'slug']
        widgets = {
            'nombre': forms.TextInput(
                attrs = {
                    "class": "form-control"
                }
            ),
            'slug': forms.TextInput(
                attrs = {
                    "class": "form-control"
                }
            ),
        }


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
        widgets = {
            'nombre': forms.TextInput(
                attrs = {
                    "class": "form-control"
                }
            ),
            'detalle': forms.Textarea(
                attrs = {
                    "class": "form-control"
                }
            ),
            'celiaco': forms.CheckboxInput(
                attrs = {
                    "class": "form-check-input"
                }
            ),
            'vegano': forms.CheckboxInput(
                attrs = {
                    "class": "form-check-input"
                }
            ),
            'delivery': forms.CheckboxInput(
                attrs = {
                    "class": "form-check-input"
                }
            ),
            'precio': forms.NumberInput(
                attrs = {
                    "class": "form-control"
                }
            ),
            'estado': forms.Select(
                attrs = {
                    "class": "form-control"
                }
            ),
            'categoria': forms.SelectMultiple(
                attrs = {
                    "class": "form-control",
                    "aria-label": "multiple select example"
                }
            ),
        }


    def __init__(self, *args, **kwargs):
        super(CargarProducto, self).__init__(*args, **kwargs)


class BuscarProducto(forms.Form):

    querycom = forms.CharField(label='Ingresar el producto',
                widget=forms.TextInput(attrs={'size': 32, 'class': 'form-control'}))