from rest_framework import viewsets, permissions
from .models import Doctor
from .serializers import DoctorSerializer

class DoctorProfileViewSet(viewsets.ModelViewSet):
    """
    A Class-Based View set for viewing and editing doctor profiles.
    """
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    
    # Permission: Only logged-in users can change data, others can only read.
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        # Automatically assign the logged-in user to the doctor profile
        serializer.save(user=self.request.user)