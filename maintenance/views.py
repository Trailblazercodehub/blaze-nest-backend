from rest_framework import viewsets
from .serializers import MaintenanceReportSerializers
from .models import MaintenanceReport

# Create your views here.
class MaintenanceReportViewSets(viewsets.ModelViewSet):
    queryset = MaintenanceReport.objects.all()
    serializer_class = MaintenanceReportSerializers
    
    