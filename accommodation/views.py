from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from .serializers import AccommodationSerializer, AccommodationListSerializer
from .models import Accommodation

# Create your views here.
class AccommodationViewSet(ModelViewSet):
    queryset = Accommodation.objects.all()
    serializer_class = AccommodationSerializer

    def list(self, request, *args, **kwargs):
        queryset = Accommodation.objects.all()
        serializer = AccommodationListSerializer(queryset, many=True)
        return Response(serializer.data)