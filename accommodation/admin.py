from django.contrib import admin
from .models import Accommodation

# Register your models here.
@admin.register(Accommodation)
class AccommodationAdmin(admin.ModelAdmin):
    pass