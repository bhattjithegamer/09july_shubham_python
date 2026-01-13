from rest_framework import serializers
from .models import Doctor

class DoctorSerializer(serializers.ModelSerializer):
    # Read-only fields to show user details inside the doctor object
    first_name = serializers.CharField(source='user.first_name', read_only=True)
    last_name = serializers.CharField(source='user.last_name', read_only=True)
    email = serializers.EmailField(source='user.email', read_only=True)

    class Meta:
        model = Doctor
        fields = [
            'id', 'user', 'first_name', 'last_name', 'email', 
            'specialization', 'license_number', 'experience_years', 
            'hospital_name', 'phone_number', 'bio'
        ]
        read_only_fields = ['user']  # Prevent changing the user association manually