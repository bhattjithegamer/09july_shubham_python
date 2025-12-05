from django.contrib import admin
from django.urls import path,include
from user import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('login/',views.login,name='login'),
    path('register/',views.register,name='register'),
    path('userlogout/',views.userlogout,name='userlogout'),
    path('update/<int:id>/',views.update,name='update'),
    path('create_post/',views.create_post,name='create_post'),
    path('delete/<int:id>/',views.delete,name='delete'),
    path('about/', views.about, name='about'),

    path('like/<int:id>/', views.like_post, name='like_post'),
    path('comment/<int:id>/', views.comment_post, name='comment_post'),
    path('follow/<int:id>/', views.follow_author, name='follow'),
    path('post/<int:id>/', views.detail_post, name='detail_post'),
]