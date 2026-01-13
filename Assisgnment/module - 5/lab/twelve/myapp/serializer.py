from rest_framework import serializers
from .models import DoctorProfile, Specialization

class SpecializationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Specialization
        fields = ['id', 'name']

class DoctorProfileSerializer(serializers.ModelSerializer):
    # These fields come from the related User model
    full_name = serializers.CharField(source='user.get_full_name', read_only=True)
    email = serializers.EmailField(source='user.email', read_only=True)
    
    # Nested serializer to show specialization names in GET requests
    specializations = SpecializationSerializer(many=True, read_only=True)
    
    # Field to allow sending IDs in POST/PUT requests
    specialization_ids = serializers.PrimaryKeyRelatedField(
        queryset=Specialization.objects.all(), 
        write_only=True, 
        many=True, 
        source='specializations'
    )

    class Meta:
        model = DoctorProfile
        fields = [
            'id', 'full_name', 'email', 'bio', 'experience_years', 
            'consultation_fee', 'specializations', 'specialization_ids', 
            'address', 'phone', 'is_verified'
        ]