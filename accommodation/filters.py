import django_filters
from .models import Accommodation

class AccommodationFilter(django_filters.FilterSet):
    price__lt = django_filters.NumberFilter(field_name='price', lookup_expr='lt')
    price__gt = django_filters.NumberFilter(field_name='price', lookup_expr='gt')

    class Meta:
        model = Accommodation
        fields = ['city', 'state', 'country', 'price', 'availability_status', 'accommodation_type']