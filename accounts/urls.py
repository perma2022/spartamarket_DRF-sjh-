from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from django.urls import path
from . import views


app_name = "accounts"

urlpatterns = [
    path("signup/", views.AccountSignupAPIView.as_view()),
    path("login/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    # path("<str:username>/", views.ProfileAPIView.as_view(), )
    path("<str:username>/", views.AccountProfileAPIView.as_view(), name="profile"),
]

