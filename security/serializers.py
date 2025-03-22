from rest_framework import serializers
from .models import SecurityReport

class SecurityReportSerializers(serializers.ModelSerializer):
    class Meta:
        model = SecurityReport
        fields = ['user', 'accommondation', 'description']