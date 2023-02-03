from django.db import models
from django.contrib.auth.models import User



class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    street = models.CharField(max_length=256)
    address = models.IntegerField()
    state = models.CharField(max_length=256)
    neighborhood = models.CharField(max_length=256)

    class Meta:
        verbose_name = 'Customer'
        verbose_name_plural = 'Customers'

    def __str__(self,):
        return f'Customer: {self.user.username}'


class Staff(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    idNumber = models.IntegerField()
    sector = models.CharField(max_length=128)

    class Meta:
        verbose_name = 'Staff'
        verbose_name_plural = 'Staff'

    def __str__(self,):
        return f'Staff: {self.user.username}'


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='users/default.png', upload_to='profile_pics/img/%Y/%m/%d')

    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'

    def __str__(self,):
        return f'Profile: {self.user.username}'