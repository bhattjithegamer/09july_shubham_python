from django.contrib import admin
from django.urls import path
from adminapp import views

urlpatterns = [
    path('admin/',admin.site.urls),
    path('admin_login/',views.admin_login,name='admin_login'),
    path('manage_users/',views.manage_users,name='manage_users'),
    path('view_bookings/',views.view_bookings,name='view_bookings'),
    path('view_reviews/',views.view_reviews,name='view_reviews'),
    path('approve_artist/',views.approve_artist,name='approve_artist'),
    path('view_feedbacks/',views.view_feedbacks,name='view_feedbacks'),
    path('admin_dashboard/',views.admin_dashboard,name='admin_dashboard')
]