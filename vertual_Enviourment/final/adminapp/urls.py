"""
URL configuration for final project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from adminapp import views
from user.views import product


urlpatterns = [
    path('admin_login/', views.admin_login, name='admin_login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('products/', views.products, name='products'),
    path('add_product/', views.add_product, name='add_product'),
    path('edit_product/<int:id>/', views.edit_product, name='edit_product'),
    path('admin_orders/', views.admin_orders, name='admin_orders'),
    path('order_details/<int:id>/', views.order_details, name='order_details'),
    path('users/', views.users, name='users'),
    path('settings/', views.settings, name='settings'),
    path('products/', views.products, name='admin_products'),
    path('update_product/<int:id>/', views.update_product, name='update_product'),
    path('delete_product/<int:id>/', views.delete_product, name='delete_product'),
    path('block_user/<int:id>/', views.block_user, name='block_user'),
    path('admin_logout/',views.admin_logout,name='admin_logout'),
    path('admin_contact_list/',views.admin_contact_list,name='admin_contact_list'),
    path('delete_contact/<int:id>/', views.delete_contact, name='delete_contact'),

]