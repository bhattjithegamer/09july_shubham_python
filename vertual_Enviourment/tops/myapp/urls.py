from django.contrib import admin
from django.urls import path,include
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='index'),
    path('login/',views.login,name='login'),
    path('signup/',views.signup,name='signup'),
    path('userlogout/',views.userlogout,name='userlogout'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('otp/',views.otp,name='otp'),
]