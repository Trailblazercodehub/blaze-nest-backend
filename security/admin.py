from django.contrib import admin
from .models import SecurityReport

# Register your models here.
@admin.register(SecurityReport)
class SecurityReportAdmin(admin.ModelAdmin):
    list_display = ('user', 'accommondation', 'description')
    search_fields = ('user__username', 'accommondation__name', 'description')
    list_filter = ('user', 'accommondation')
    
    