from django.urls import path
from .views import (
    admin_statistics,
    admin_list_products,
    admin_add_product,
    admin_edit_product,
    admin_delete_product,
    admin_list_orders,
    admin_update_order,
    admin_login,
    admin_change_password,

)

urlpatterns = [
    path('stats/',admin_statistics,name='admin_stats'),
    path('products/',admin_list_products,name='admin_products'),
    path('products/add/',admin_add_product,name='admin_add_product'),
    path('products/edit/<int:pk>/',admin_edit_product,name='admin_edit_product'),
    path('product-delete/<int:pk>/',admin_delete_product,name='admin_delete_product'),
    path('orders/',admin_list_orders,name='admin_orders'),
    path('orders/update/<int:pk>/',admin_update_order,name='admin_update_order'),
    path('admin-login/', admin_login,name='admin_login'),
    path('admin-change-password/', admin_change_password),
]