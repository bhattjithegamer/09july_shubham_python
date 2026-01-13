from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import DoctorProfile
from .serializer import DoctorProfileSerializer

class DoctorViewSet(viewsets.ModelViewSet):
    queryset = DoctorProfile.objects.all().select_related('user').prefetch_related('specializations')
    serializer_class = DoctorProfileSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['specializations__name', 'experience_years']
    search_fields = ['user__first_name', 'user__last_name', 'bio']
    ordering_fields = ['consultation_fee', 'experience_years']