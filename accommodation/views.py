from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import filters
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import AccommodationSerializer, AccommodationListSerializer
from .models import Accommodation
from .filters import AccommodationFilter

# Create your views here.
class AccommodationViewSet(ModelViewSet):
    queryset = Accommodation.objects.all()
    serializer_class = AccommodationSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['city', 'state', 'country', 'price', 'availability_status', 'accommodation_type']
    filter_class = AccommodationFilter
    search_fields = ['name', 'description', 'amenities']
    ordering_fields = ['price', 'rating']
    permission_classes = [IsAuthenticatedOrReadOnly]

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = AccommodationListSerializer(queryset, many=True)
        return Response(serializer.data)

        