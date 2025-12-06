from django.contrib import admin
from django.urls import path,include
from adminapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.admin_login,name='admin_login'),
    path('admin_dashboard/',views.admin_dashboard,name='admin_dashboard'),
    path('admin_userdata/',views.admin_userdata,name='admin_userdata'),
    path('admin_notesdata/',views.admin_notesdata,name='admin_notesdata'),
    path('adminlogout/',views.adminlogout,name='adminlogout'),
    path('admin_product/',views.admin_product,name='admin_product'),
    path('admin_add_pro/',views.admin_add_pro,name='admin_add_pro'),
    path('deleteproduct/<int:id>/',views.deleteproduct,name='deleteproduct'),
    path('notes_approve/<int:id>/',views.notes_approve,name='notes_approve'),
    path('notes_reject/<int:id>/',views.notes_reject,name='notes_reject'),
]