from django.urls import path
from .views import country_info

urlpatterns = [
    path('', country_info, name='country_info'),
]