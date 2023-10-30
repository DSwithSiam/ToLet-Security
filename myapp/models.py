from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Service(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    icon = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

#user Profile databse table
class UserData (models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    user_firstname = models.CharField(max_length=100)
    user_lastname = models.CharField(max_length=100)
    user_address = models.CharField(max_length=200)
    user_state = models.CharField(max_length=100)
    user_area = models.CharField(max_length=100)
    user_postcode = models.CharField(max_length=10)
    user_phone = models.CharField(max_length=20)
    user_education = models.CharField(max_length=120)
