from django.contrib import admin

# Register your models here.
from .models import Donor
from .models import BloodDonate

# Register your site here.
admin.site.register(Donor)
admin.site.register(BloodDonate)
