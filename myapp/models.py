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

class UserData (models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
