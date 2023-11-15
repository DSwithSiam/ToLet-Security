from django.db import models
from django.contrib.auth.models import User
from PIL import Image


# Create your models here.
class Service(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    icon = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='no-image.jpg', upload_to='profile')

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        # save the profile first
        super().save(*args, **kwargs)

        # resize the image
        img = Image.open(self.avatar.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            # create a thumbnail
            img.thumbnail(output_size)
            # overwrite the larger image
            img.save(self.avatar.path)

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
