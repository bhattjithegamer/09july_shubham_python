from django.urls import path
from .views import checkout_page, create_checkout_session, payment_success, payment_cancelled

urlpatterns = [
    path('', checkout_page, name='checkout_page'),
    path('payment/create-session/', create_checkout_session, name='create_checkout_session'),
    path('payment/success/', payment_success, name='payment_success'),
    path('payment/cancelled/', payment_cancelled, name='payment_cancelled'),
]