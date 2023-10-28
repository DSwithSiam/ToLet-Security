from django.db import models

# Create your models here.
class Service(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    icon = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Property(models.Model):
    status = models.CharField(max_length=120)
    lift = models.BooleanField(default=False)
    gas = models.BooleanField(default=False)
    propertyType = models.CharField(max_length=100)
    division = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    squareFeet = models.IntegerField()
    bedRoom = models.IntegerField()
    drawingRoom = models.IntegerField()
    diningRoom = models.IntegerField()
    balcony = models.IntegerField()
    washRoom = models.IntegerField()
    areaName = models.TextField()
    rules = models.TextField()
    image = models.ImageField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
