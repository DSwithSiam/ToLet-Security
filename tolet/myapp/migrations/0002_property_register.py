# Generated by Django 4.2.6 on 2023-10-28 22:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=120)),
                ('lift', models.BooleanField(default=False)),
                ('gas', models.BooleanField(default=False)),
                ('propertyType', models.CharField(max_length=100)),
                ('division', models.CharField(max_length=100)),
                ('district', models.CharField(max_length=100)),
                ('squareFeet', models.IntegerField()),
                ('bedRoom', models.IntegerField()),
                ('drawingRoom', models.IntegerField()),
                ('diningRoom', models.IntegerField()),
                ('balcony', models.IntegerField()),
                ('washRoom', models.IntegerField()),
                ('areaName', models.TextField()),
                ('rules', models.TextField()),
                ('image', models.ImageField(upload_to='')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Register',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('phone', models.CharField(max_length=25)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=30)),
            ],
        ),
    ]
