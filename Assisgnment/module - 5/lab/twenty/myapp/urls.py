from django.urls import path
from .views import send_otp, verify_otp

urlpatterns = [
    path('', send_otp, name='send_otp'),
    path('otp/verify/', verify_otp, name='verify_otp'),
]