from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from PIL import Image


# Create your models here.
class Division(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name

    def get_districts_url(self):
        return reverse('get_districts', args=[str(self.id)])


class District(models.Model):
    name = models.CharField(max_length=255)
    division = models.ForeignKey(Division, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} - {self.division}"

    def get_upazilas_url(self):
        return reverse('get_upazilas', args=[str(self.id)])


class Upazila(models.Model):
    name = models.CharField(max_length=255)
    district = models.ForeignKey(District, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} - {self.district}"


#username, email, first_name, last_name, groups, user_permissions
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15)
    profile_picture = models.ImageField(default='no-image.png', upload_to='profile')
    division = models.ForeignKey(Division, on_delete=models.SET_NULL, null=True)
    district = models.ForeignKey(District, on_delete=models.SET_NULL, null=True)
    upazila = models.ForeignKey(Upazila, on_delete=models.SET_NULL, null=True)
    area = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        # save the profile first
        super().save(*args, **kwargs)

        # resize the image
        img = Image.open(self.profile_picture.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            # create a thumbnail
            img.thumbnail(output_size)
            # overwrite the larger image
            img.save(self.profile_picture.path)