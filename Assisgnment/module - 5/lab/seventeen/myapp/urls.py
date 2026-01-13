from django.urls import path
from .views import fetch_tweets

urlpatterns = [
    path('', fetch_tweets, name='fetch_tweets'),
]