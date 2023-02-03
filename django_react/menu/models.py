from django.db import models
from users.models import Staff
import datetime


class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return f'Category: {self.name}'

class Meal(models.Model):

    no_stock = 'No stock'
    published = 'Published'
    paused = 'Paused'
    STATE = (
        (no_stock, 'No stock'),
        (published, 'Published'),
        (paused, 'Paused'),
    )

    creationDate = models.DateTimeField(default=datetime.datetime.today)
    modificationDate = models.DateTimeField(auto_now=True)
    
    staff = models.ForeignKey(Staff, on_delete=models.SET_NULL, blank=True, null=True)
    
    name = models.CharField(max_length=200) 
    description = models.TextField(max_length=300)
    celiac = models.BooleanField(default=False)
    vegan = models.BooleanField(default=False)
    delivery = models.BooleanField(default=False)
    image = models.FileField(
        upload_to='menu/img/%Y/%m/%d', 
        default='menu/default.png',
        blank=True,
        null=True
    )
    category = models.ManyToManyField(Category)
    price = models.FloatField()
    publication = models.CharField(max_length=200, choices=STATE, default=paused)

    def __str__(self):
        return f'Meal: {self.name}'