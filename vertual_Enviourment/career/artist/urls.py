from django.contrib import admin
from django.urls import path
from artist import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('artist_home',views.artist_home,name='artist_home'),
    path('artist_register/',views.artist_register,name='artist_register'),
    path('artist_login/',views.artist_login,name='artist_login'),
    path('artist_manage_profile/',views.artist_manage_profile,name='artist_manage_profile'),
    path('artist_upload_media/',views.artist_upload_media,name='artist_upload_media'),
    path('artist_feedback/',views.artist_feedback,name='artist_feedback'),
    path('artist_view_booking/',views.artist_view_booking,name='artist_view_booking'),
    path('delete_booking/<int:id>/', views.delete_booking, name='delete_booking'),

]