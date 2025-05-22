from rest_framework import serializers
from .models import Booking
from accommodation.serializers import AccommodationSerializer  # Import your accommodation serializer

class BookingSerializer(serializers.ModelSerializer):
    accommodation_details = serializers.SerializerMethodField()
    
    class Meta:
        model = Booking
        fields = ['id', 'user', 'accommondation', 'accommodation_details', 'total_amount', 'created_at']
        read_only_fields = ['user', 'created_at']
    
    def get_accommodation_details(self, obj):
        if obj.accommondation:
            return AccommodationSerializer(obj.accommondation).data
        return None
    
    def validate(self, data):
        # Add any custom validation you need
        if data['accommondation'] and data['accommondation'].available is False:
            raise serializers.ValidationError("This accommodation is not available for booking")
        return data