from django.urls import path
from .views import DoctorCreateAPIView

urlpatterns = [
    path('', DoctorCreateAPIView.as_view(), name='doctor-create'),
]
