from django.urls import path
from adminapp import views


urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('posts/', views.all_posts, name='all_posts'),

]
