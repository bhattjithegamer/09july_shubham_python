from rest_framework import serializers
from .models import Specialization, DoctorProfile  

class SpecializationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Specialization
        fields = ['id', 'name']

class DoctorProfileSerializer(serializers.ModelSerializer):
    full_name = serializers.CharField(source='user.get_full_name', read_only=True)
    email = serializers.EmailField(source='user.email', read_only=True)
    specializations = SpecializationSerializer(many=True, read_only=True)
    specialization_ids = serializers.PrimaryKeyRelatedField(
        queryset=Specialization.objects.all(), write_only=True, many=True, source='specializations'
    )

    class Meta:
        model = DoctorProfile
        fields = [
            'id', 'full_name', 'email', 'bio', 'experience_years', 
            'consultation_fee', 'specializations', 'specialization_ids', 
            'address', 'phone', 'is_verified'
        ]