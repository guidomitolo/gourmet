from django.db.models.signals import post_save, pre_save

from django.contrib.auth import get_user_model
User = get_user_model()

from django.dispatch import receiver
from .models import Profile

# el remitente es el usuario creado tras las registración y el receptor es la funcion
@receiver(post_save, sender=User)
# se crea el perfil del remitente
def create_profile(sender, instance, created, **kwargs):
  # si no está creado el perfil, se crea
  if created:
    # para el metodo create, el parametro es el objecto creado
    Profile.objects.create(user=instance)

# lo mismo, pero para guardar el perfil
@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
  profile = Profile()
  instance.profile.save()

