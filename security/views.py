from rest_framework import viewsets
from .serializers import SecurityReportSerializers
from .models import SecurityReport

# Create your views here.
class SecurityReportViewSet(viewsets.ModelViewSet):
    queryset = SecurityReport.objects.all()
    serializer_class = SecurityReportSerializers
    
