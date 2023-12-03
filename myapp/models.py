from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from ckeditor.fields import RichTextField


# Create your models here.
class Service(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    icon = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


# Add Property
class Add_property(models.Model):
    propertytype = models.CharField(max_length=100)
    division = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    areaname = models.CharField(max_length=100)
    images = models.ImageField(upload_to='addproperty')


# class Add_property(models.Model):

#     # property Information
#     status = models.CharField(max_length=100)
#     propertytype = models.CharField(max_length=100)
#     size = models.CharField(max_length=100)
#     bedroom = models.CharField(max_length=100)
#     drawingroom = models.CharField(max_length=100)
#     diningroom = models.CharField(max_length=100)
#     balcony = models.CharField(max_length=100)
#     washroom = models.CharField(max_length=100)
#     rules = models.CharField(max_length=100)
#     comment = models.CharField(max_length=100)

#     # Add Location
#     division = models.CharField(max_length=100)
#     district = models.CharField(max_length=100)
#     areaname = models.CharField(max_length=100)

#     # Facilities
#     lift = models.BooleanField()
#     gas = models.BooleanField()
#     garage = models.BooleanField()
#     cc_camera = models.BooleanField()
#     security_guard = models.BooleanField()
#     swiming_pool = models.BooleanField()
#     store_room = models.BooleanField()
#     fire_extinguisher = models.BooleanField()

#     # Add Images
#     images = models.ImageField(upload_to='add_property')

#     # Owner Information
#     owner_name = models.CharField(max_length=100)
#     contact_number = models.IntegerField()
#     whatsapp_number = models.IntegerField()


class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    message = models.TextField()
    contacted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class PrivacyPolicy(models.Model):
    title = models.CharField(max_length=200)
    content = RichTextField()
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Privacy Policy"
        verbose_name_plural = "Privacy Policy"


class TermsAndConditions(models.Model):
    title = models.CharField(max_length=200)
    content = RichTextField()
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Terms And Condition"
        verbose_name_plural = "Terms And Conditions"


class FAQ(models.Model):
    question = models.CharField(max_length=255)
    answer = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.question
