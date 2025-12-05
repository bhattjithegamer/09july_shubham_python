from django.urls import path
from adminapp import views


urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('posts/', views.all_posts, name='all_posts'),
    path('users/', views.users_list, name='users_list'),
    path('delete-user/<int:id>/', views.delete_user, name='delete_user'),

]
