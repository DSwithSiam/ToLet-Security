from django.contrib import admin
from myapp.models import *


# Register your models here.
# To view data in tables form in Database
# class Addproperty(admin.ModelAdmin):
#     list_display = ('id', 'propertytype', 'division',
#                     'district', 'areaname', 'images')
#     # it’s must be list or tuple




# class Add_property(admin.ModelAdmin):
#     list_display = ('id', 'status', 'propertytype',
#                     'size', 'bedroom', 'drawingroom', 'diningroom', 'balcony',
#                     'washroom', 'rules', 'comment', 'division', 'district',
#                     'areaname', 'lift', 'gas', 'garage', 'cc_camera',
#                     'security_guard', 'swiming_pool', 'store_room', 'fire_extinguisher', 'images', 'owner_name', 'contact_number', 'whatsapp_number')
#     # it’s must be list or tuple
    
    
admin.site.register(Add_property)
admin.site.register(Service)
