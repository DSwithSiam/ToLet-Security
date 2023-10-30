from django.contrib import admin
from myapp.models import *


# Register your models here.
admin.site.register(Service)
admin.site.register(UserData)
class std_UserData(admin.ModelAdmin):
    list_display = ('user', 'user_firstname', 'user_lastname', 'user_address', 'user_state', 'user_area', 'user_postcode', 'user_phone', 'user_education')