from rest_framework import serializers
from .models import Booking

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ['id', 'user', 'accommondation', 'total_amount', 'created_at']
        read_only_fields = ['user', 'created_at']