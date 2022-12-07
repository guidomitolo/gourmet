from django.db import models
from django.contrib.auth.models import AbstractUser
from PIL import Image


class User(AbstractUser):
    # username and password -> default
    username = models.CharField(max_length=30, unique=False)
    email = models.EmailField(max_length=100, unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    is_customer = models.BooleanField("Cliente",default=False)
    is_employee = models.BooleanField("Empleado",default=False)
    is_guest = models.BooleanField("Invitado",default=False)


class Cliente(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    telefono = models.CharField(max_length=20)

    calle = models.CharField(max_length=200, null=True)
    altura = models.IntegerField(null=True)
    localidad = models.CharField(max_length=200, null=True)
    municipio = models.CharField(max_length=200, null=True)

    def __str__(self,):
        return f'{self.user.username}'


class Empleado(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    telefono = models.CharField(max_length=20)

    def __str__(self,):
        return f'{self.user.username}'


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='users/default.jpg', upload_to='profile_pics/img/%Y/%m/%d')

    def __str__(self,):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):

        super(Profile, self).save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)