from django.contrib import admin
from .models import Vendor

# Register your models here.
@admin.register(Vendor)
class VendorAdmin(admin.ModelAdmin):
    list_display = ('business_name', 'email', 'is_verified', 'date_joined')
    search_fields = ('business_name', 'email')
    list_filter = ('is_verified', 'date_joined')
    ordering = ('-date_joined',)
    list_per_page = 20
