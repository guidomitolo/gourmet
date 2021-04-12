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


def save(self, *args, **kwargs):
    ## Clean previous file
    try:
        this = Profile.objects.get(id=self.id)
        if this.image != self.image:
            this.image.delete(save=False)
    except: pass

    super(Profile, self).save(*args, **kwargs)

    if img.height > 300 or img.width > 300:
        output_size = (300, 300)
        img.thumbnail(output_size)
        img.save(self.image.path)

##############################3333
# creo nuevo modelo para poder listar usuarios en formulario
# class EmpleadosRegistrados(models.Model):
    
#     # user = models.OneToOneField(Empleado.user.username, on_delete=models.CASCADE, primary_key=True)
#     active = models.OneToOneField(Empleado.user.is_active, on_delete=models.CASCADE, primary_key=True)

#     def __str__(self):
#         return f'{self.user.username}'
