from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    is_customer = models.BooleanField(default=False)
    is_employee = models.BooleanField(default=False)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)


class Cliente(models.Model):
    # https://docs.djangoproject.com/en/2.2/topics/auth/customizing/#extending-the-existing-user-model
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    phone = models.CharField(max_length=20)
    location = models.CharField(max_length=20)

    def __str__(self,):
        return f'{self.user.username}'


class Empleado(models.Model):
    # https://docs.djangoproject.com/en/2.2/topics/auth/customizing/#extending-the-existing-user-model
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    phone = models.CharField(max_length=20)

    def __str__(self,):
        return f'{self.user.username}'


class Profile(models.Model):
    # relacion uno a uno con Usuario. si usuario es eliminado, se elimina el perfil
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # pip install pillow
    image = models.ImageField(default='users/default.jpg', upload_to='profile_pics')

    def __str__(self,):
        return f'{self.user.username} Profile'