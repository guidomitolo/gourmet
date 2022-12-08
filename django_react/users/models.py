from django.db import models
from django.contrib.auth.models import User
from PIL import Image



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
        return self.user.username


class Staff(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    idNumber = models.IntegerField()
    sector = models.CharField(max_length=128)

    class Meta:
        verbose_name = 'Staff'
        verbose_name_plural = 'Staff'

    def __str__(self,):
        return self.user.username


class Profile(User):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="AppUser")
    image = models.ImageField(default='users/default.jpg', upload_to='profile_pics/img/%Y/%m/%d')

    def __str__(self,):
        return self.user.username

    def save(self, *args, **kwargs):

        super(Profile, self).save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)