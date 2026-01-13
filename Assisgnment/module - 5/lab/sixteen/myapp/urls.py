from django.urls import path
from .views import github_manager

urlpatterns = [
    path('', github_manager, name='github_manager'),
]