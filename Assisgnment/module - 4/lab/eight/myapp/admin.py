from django.contrib import admin
from .models import Doctor

@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('name', 'specialty', 'experience', 'hospital', 'contact')
    search_fields = ('name', 'specialty', 'hospital')
    list_filter = ('specialty', 'hospital')
    ordering = ('name',)
    list_per_page = 10
