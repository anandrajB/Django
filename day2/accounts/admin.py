from django.contrib import admin
from .models import Principal , School , student , Staff

# Register your models here.
admin.site.register(Principal)
admin.site.register(student)
admin.site.register(Staff)
admin.site.register(School)