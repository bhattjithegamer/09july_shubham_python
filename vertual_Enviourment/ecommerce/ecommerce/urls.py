from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve 
from django.urls import re_path 
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from myapp.views import (
    get_products,
    google_login,
    register_user,
    get_user_profile,
    update_user_profile,
    get_user_orders,
    create_payment_order,
    handle_payment_success,
    handle_payment_failure,
    get_product_details,
    custom_login,
    clear_order_history,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('get_products/', get_products, name='get_products'),

    # AUTH
    path('api/register/', register_user, name='register'),
    path('api/login/', custom_login, name='login'),          # ← custom_login (is_admin return )
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/google-login/', google_login, name='google_login'),

    # PROFILE
    path('api/profile/', get_user_profile, name='user_profile'),
    path('api/profile/update/', update_user_profile, name='update_profile'),

    # ORDERS
    path('api/orders/', get_user_orders, name='user_orders'),
    path('api/orders/clear/', clear_order_history),

    # PAYMENTS
    path('api/create-payment/', create_payment_order, name='create_payment'),
    path('api/payment-success/', handle_payment_success, name='payment_success'),
    path('api/payment-failure/', handle_payment_failure, name='payment_failure'),

    # PRODUCT DETAIL
    path('api/products/<int:pk>/', get_product_details, name='product_details'),

    # DASHBOARD (admin panel APIs) — 'api/stats/' prefix
    path('api/stats/', include('dashboard.urls')),
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)