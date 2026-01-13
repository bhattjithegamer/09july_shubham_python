from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import RegisterView, LogoutView

urlpatterns = [
    # 1. Registration
    path('register/', RegisterView.as_view(), name='auth_register'),
    
    # 2. Login (Tokens મેળવવા માટે)
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    
    # 3. Token Refresh (જ્યારે access token એક્સપાયર થાય)
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    # 4. Logout
    path('logout/', LogoutView.as_view(), name='auth_logout'),
]