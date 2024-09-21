from django.contrib import admin

# Register your models here.

from .models import Patient

# Register your site here.

admin.site.register(Patient)
