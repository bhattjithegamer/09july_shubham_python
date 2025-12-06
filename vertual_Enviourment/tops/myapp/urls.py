from django.contrib import admin
from django.urls import path,include
from myapp import views
from django.conf import settings              
from django.conf.urls.static import static 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='index'),
    path('login/',views.login,name='login'),
    path('signup/',views.signup,name='signup'),
    path('userlogout/',views.userlogout,name='userlogout'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('otp/',views.otp,name='otp'),
    path('notes/',views.notes,name='notes'),
    path('cart/',views.cart,name='cart'),
    path('profile/',views.profile,name="profile"),
    path('add_to_cart/<int:id>/', views.add_to_cart, name='add_to_cart'),
    path('update_cart/<int:id>/', views.update_cart, name='update_cart'),
    path('remove_cart/<int:id>/', views.remove_cart, name='remove_cart'),
    path('increase_cart/<int:id>/', views.increase_cart, name='increase_cart'),
    path('decrease_cart/<int:id>/', views.decrease_cart, name='decrease_cart'),  
    path('update_profile/<int:id>/',views.update_profile,name='update_profile'),
    path('proced/',views.proced,name='proced'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)