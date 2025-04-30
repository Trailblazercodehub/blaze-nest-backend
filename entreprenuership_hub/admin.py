from django.contrib import admin
from .models import Event, CoWorking, CoWorkingApplication, Incubator, IncubatorApplication

# Register your models here.
@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'date', 'location', 'created_at')
    search_fields = ('title', 'description', 'location')
    list_filter = ('date',)
    ordering = ('-created_at',)
    
@admin.register(CoWorking)
class CoWorkingAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'location', 'created_at')
    search_fields = ('name', 'description', 'location')
    list_filter = ('created_at',)
    ordering = ('-created_at',)
    
@admin.register(CoWorkingApplication)
class CoWorkingApplicationAdmin(admin.ModelAdmin):
    list_display = ('user', 'coworking', 'message', 'created_at')
    search_fields = ('user__email', 'coworking__name', 'message')
    list_filter = ('created_at',)
    ordering = ('-created_at',)
    
@admin.register(Incubator)
class IncubatorAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'location', 'created_at')
    search_fields = ('name', 'description', 'location')
    list_filter = ('created_at',)
    ordering = ('-created_at',)
    
@admin.register(IncubatorApplication)
class IncubatorApplicationAdmin(admin.ModelAdmin):
    list_display = ('user', 'incubator', 'message', 'created_at')
    search_fields = ('user__email', 'incubator__name', 'message')
    list_filter = ('created_at',)
    ordering = ('-created_at',)
    
    

