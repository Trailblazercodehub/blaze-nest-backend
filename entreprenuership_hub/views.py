from rest_framework import viewsets
from .models import CoWorking, CoWorkingApplication, \
Event, Incubator, IncubatorApplication
from .serializers import CoWorkingSerializer, CoWorkingApplicationSerializer, \
EventSerializer, IncubatorSerializer, IncubatorApplicationSerializer


# Create your views here.
class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    
class CoWorkingViewSet(viewsets.ModelViewSet):
    queryset = CoWorking.objects.all()
    serializer_class = CoWorkingSerializer
    
class IncubatorViewSet(viewsets.ModelViewSet):
    queryset = Incubator.objects.all()
    serializer_class = IncubatorSerializer
    
class IncubatorApplicationViewSet(viewsets.ModelViewSet):
    queryset = IncubatorApplication.objects.all()
    serializer_class = IncubatorApplicationSerializer
    
class CoWorkingApplicationViewSet(viewsets.ModelViewSet):
    queryset = CoWorkingApplication.objects.all()
    serializer_class = CoWorkingApplicationSerializer
    
