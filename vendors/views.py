from rest_framework import viewsets
from .models import Vendor
from .serializers import VendorSerializer
from .permissions import IsVendor
from rest_framework.permissions import AllowAny

class VendorViewSet(viewsets.ModelViewSet):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer
    # permission_classes = [IsVendor]
