from django.contrib import admin

# Register your models here.
from .models import Stock
from .models import BloodRequest

# Register your site here.
admin.site.register(Stock)
admin.site.register(BloodRequest)