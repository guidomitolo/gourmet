from django.forms import ModelForm
from main.models import Consulta

class ConsultaForm(ModelForm):

    class Meta:
        model = Consulta
        fields = ['nombre', 'mail', 'descripcion']
        # todos los campos son requeridos
        error_messages = {
            'nombre': {
                'required': ("Por favor completar su nombre"),
            },
            'mail': {
                'required': ("Por favor completar con un correo válido"),
            },
            'descripcion': {
                'required': ("Completar mensaje"),
            },
        }

    def __init__(self, *args, **kwargs):
        super(ConsultaForm, self).__init__(*args, **kwargs)