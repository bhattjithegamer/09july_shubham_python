from django.shortcuts import render
from rest_framework import viewsets,permissions
from .models import *
from .serializers import *
from rest_framework.permissions import IsAuthenticated  # Example



class TaskPermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.role == 'admin':
            return True
        return obj.assigned_to == request.user
    
class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = taskserializer
    permission_classes = [permissions.IsAuthenticated, TaskPermission]
    queryset = task.objects.all()

    def get_queryset(self):
        user = self.request.user
        if user.role == 'admin':
            return task.objects.all()
        return task.objects.filter(assigned_to=user)

class UserViewSet(viewsets.ModelViewSet):
    serializer_class = userserializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = user.objects.all()

    def get_queryset(self):
        user = self.request.user
        if user.role == 'admin':
            return user.objects.all()
        return user.objects.filter(id=user.id)


# Create your views here.
