from django.urls import path
from apps.acount.view import RegistrationAPIView

urlpatterns = [
    path('users/', RegistrationAPIView.as_view()),
]