from django.contrib import admin
from myapp.models import *


# Register your models here.
# To view data in tables form in Database
class Addproperty(admin.ModelAdmin):
    list_display = ('id', 'propertytype', 'division',
                    'district', 'areaname', 'images')
    # it’s must be list or tuple


admin.site.register(Service)
admin.site.register(Add_property, Addproperty)
