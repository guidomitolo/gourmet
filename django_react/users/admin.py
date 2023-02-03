from django.contrib import admin
from .models import Customer, Staff, Profile

admin.site.register(Customer)
admin.site.register(Staff)

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    fields = ['user','image']