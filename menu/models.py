from django.db import models
# configuración del sitio de administración
from django.utils.html import format_html

# importo User para relacionarlo con el modelo Producto
from gourmet import settings

# importo datetime para guardar fecha de creación de la entrada
import datetime


from PIL import Image


class Categoria(models.Model):
    nombre = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, db_index=True)

    def __str__(self):
        return f'{self.nombre}'

class Producto(models.Model):

    sin_stock = 'Sin stock'
    publicado = 'Publicado'
    pausado = 'Pausado'
    ESTADO_PRODUCTO = (
        (sin_stock, 'Sin stock'),
        (publicado, 'Publicado'),
        (pausado, 'Pausado'),
    )

    # control de tiempos
    pub_date = models.DateField(default=datetime.datetime.today)
    last_modified = models.DateTimeField(auto_now=True) # cuando se creó/modificó el registro
    
    # to set the ForeignKey to null when the referenced object is deleted
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.SET_NULL, blank=True, null=True)
    
    nombre = models.CharField(max_length=200) # nombre del plato
    detalle = models.TextField(max_length=300)
    celiaco = models.BooleanField("Apto celíaco", default=False)
    vegano = models.BooleanField("Vegano", default=False)
    delivery = models.BooleanField("Delivery", default=False)
    ruta_imagen = models.FileField(upload_to='menu/img/%Y/%m/%d', 
                                    default='menu/default.png',
                                    blank=True,
                                    null=True)
    categoria = models.ManyToManyField(Categoria)
    precio = models.FloatField()
    estado = models.CharField(max_length=200, choices=ESTADO_PRODUCTO, default='Pausado')

    def estado_producto(self):
        if self.estado == 'Sin stock':
            return format_html('<span style="color: #f00;">{}</span>', self.estado)
        elif self.estado == 'Pausado':
            return format_html('<span style="color: #f0f;">{}</span>', self.estado)
        elif self.estado == 'Publicado':
            return format_html('<span style="color: #099;">{}</span>', self.estado)

    def __str__(self):
        return f'{self.nombre}'


    def save(self, *args, **kwargs):

        super(Producto, self).save(*args, **kwargs)

        img = Image.open(self.ruta_imagen.path)

        if img.height > 250 or img.width > 250:
            output_size = (250,250)
            img.thumbnail(output_size)
            img.save(self.ruta_imagen.path)