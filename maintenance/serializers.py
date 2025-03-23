from rest_framework import serializers
from .models import MaintenanceReport

class MaintenanceReportSerializers(serializers.ModelSerializer):
    class Meta:
        model = MaintenanceReport
        fields = ['user', 'accommondation', 'description']
        
