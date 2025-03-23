from rest_framework import serializers
from .models import CoWorking, CoWorkingApplication, \
Event, Incubator, IncubatorApplication

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ['id', 'title', 'description', 'date', 'location', 'image', 'created_at']
        
class CoWorkingSerializer(serializers.ModelSerializer):
    class Meta:
        model = CoWorking
        fields = ['id', 'name', 'description', 'users', 'location', 'image', 'created_at']
        
class IncubatorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Incubator
        fields = ['id', 'name', 'description', 'users', 'location', 'image', 'created_at']
        
class IncubatorApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = IncubatorApplication
        fields = ['id', 'user', 'incubator', 'message', 'created_at']
        
        
class CoWorkingApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = CoWorkingApplication
        fields = ['id', 'user', 'coworking', 'message', 'created_at']
        
