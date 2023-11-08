from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Materials,Purpose,Order

# Register your models here.
admin.site.register(Purpose)
admin.site.register(Materials)
admin.site.register(Order)