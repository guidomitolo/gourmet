# Generated by Django 2.2 on 2021-04-09 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_delete_empleadosregistrados'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='users/default.jpg', upload_to='profile_pics'),
        ),
    ]