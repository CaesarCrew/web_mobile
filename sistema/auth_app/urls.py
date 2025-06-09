from django.urls import path
from .views import LoginView, LoginAPI

urlpatterns = [
    path('', LoginView.as_view(), name='login'),
    path('api/login/', LoginAPI.as_view(), name='api_login'),
]