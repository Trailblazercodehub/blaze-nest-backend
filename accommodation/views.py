from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializers import AccommodationSerializer
from .models import Accommodation

# Create your views here.
class AccommodationViewSet(ModelViewSet):
    queryset = Accommodation.objects.all()
    serializer_class = AccommodationSerializer