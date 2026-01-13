from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_joke, name='get_joke'),
]
