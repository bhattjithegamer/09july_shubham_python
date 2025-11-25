from django.shortcuts import render
from .models import Doctor

def index(request):
    doctors = Doctor.objects.all()
    return render(request,'index.html', {'doctors': doctors})
