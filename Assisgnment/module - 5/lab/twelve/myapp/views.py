from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import DoctorProfile
from .serializer import DoctorProfileSerializer

class DoctorViewSet(viewsets.ModelViewSet):
    queryset = DoctorProfile.objects.all().select_related('user').prefetch_related('specializations')
    serializer_class = DoctorProfileSerializer
    
    # Adding Search and Filter capabilities
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['experience_years', 'is_verified']
    search_fields = ['user__first_name', 'user__last_name', 'bio', 'specializations__name']
    ordering_fields = ['consultation_fee', 'experience_years']