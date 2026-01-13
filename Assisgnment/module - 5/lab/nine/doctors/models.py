# doctors/models.py
from django.db import models

class DoctorProfile(models.Model):
    SPECIALTIES = [
        ('Cardiology', 'Cardiology'),
        ('Dermatology', 'Dermatology'),
        ('Pediatrics', 'Pediatrics'),
        ('Neurology', 'Neurology'),
        ('General', 'General Practice'),
    ]

    full_name = models.CharField(max_length=200)
    specialty = models.CharField(max_length=50, choices=SPECIALTIES)
    license_number = models.CharField(max_length=50, unique=True)
    bio = models.TextField(blank=True)
    contact_number = models.CharField(max_length=15)
    email = models.EmailField()
    profile_picture = models.ImageField(upload_to='doctor_profiles/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Dr. {self.full_name} ({self.specialty})"