from django.contrib import admin
from myapp.models import *


admin.site.site_header = "ToLet & Security"


# Register your models here.

# class addproperty(admin.ModelAdmin):
#     list_display = ('id', 'status', 'propertytype',
#                     'size', 'bedroom', 'drawingroom', 'diningroom', 'balcony',
#                     'washroom', 'rules', 'comment', 'division', 'district',
#                     'areaname', 'lift', 'gas', 'garage', 'cc_camera',
#                     'security_guard', 'swiming_pool', 'store_room', 'fire_extinguisher', 'images', 'owner_name', 'contact_number', 'whatsapp_number')
#     # it’s must be list or tuple


admin.site.register(Add_property)
admin.site.register(Service)
admin.site.register(Contact)
admin.site.register(PrivacyPolicy)
admin.site.register(TermsAndConditions)
admin.site.register(FAQ)
