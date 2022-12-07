from gourmet import settings
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

User = get_user_model()

class Command(BaseCommand):

    def handle(self, *args, **options):
        if User.objects.count() == 0:
            username = settings.ADMIN_USERNAME
            email = settings.ADMIN_EMAIL
            password = settings.ADMIN_INITIAL_PASSWORD
            print(f'Creando superusuario para {username} ({email})')
            admin = User.objects.create_superuser(
                email=email,
                username=username,
                password=password
            )
            admin.is_active = True
            admin.is_admin = True
            admin.save()
        else:
            print('Ya se han iniciado otras cuentas de usuario')