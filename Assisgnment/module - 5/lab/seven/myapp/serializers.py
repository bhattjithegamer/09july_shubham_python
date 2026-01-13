from rest_framework import serializers
from .models import DoctorProfile

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = DoctorProfile
        fields = '__all__'