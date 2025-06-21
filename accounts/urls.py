from django.urls import path
from .views import public_view, protected_view,test_email_task
from rest_framework_simplejwt.views import (
    TokenObtainPairView,TokenRefreshView,
)

urlpatterns = [
    path('public/', public_view),
    path('protected/', protected_view),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('test-email/', test_email_task),
]
