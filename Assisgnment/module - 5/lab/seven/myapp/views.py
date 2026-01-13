from rest_framework import generics
from .models import DoctorProfile
from .serializers import DoctorSerializer
from .pagination import DoctorPagination

class DoctorListView(generics.ListAPIView):
    queryset = DoctorProfile.objects.all()
    serializer_class = DoctorSerializer
    pagination_class = DoctorPagination 