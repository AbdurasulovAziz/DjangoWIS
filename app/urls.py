from django.urls import path
from app.views import UserRegistrationView


urlpatterns = [
    path('registration', UserRegistrationView.as_view(), name='registration')
]
