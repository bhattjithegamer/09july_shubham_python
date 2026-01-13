# doctors/admin.py
from django.contrib import admin
from .models import DoctorProfile

admin.site.register(DoctorProfile)