from rest_framework import serializers
from .models import Vendor

class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = ['user', 'email', 'business_name', 'phone_number', 'address', 'is_verified', 'date_joined']
