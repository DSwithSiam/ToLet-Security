# Generated by Django 4.2.5 on 2023-11-06 15:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('myapp', '0002_userdata'),
    ]

    operations = [
        migrations.CreateModel(
            name='Add_property',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('propertytype', models.CharField(max_length=100)),
                ('division', models.CharField(max_length=100)),
                ('district', models.CharField(max_length=100)),
                ('areaname', models.CharField(max_length=100)),
                ('images', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='no-image.jpg', upload_to='profile')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='UserData',
        ),
    ]
