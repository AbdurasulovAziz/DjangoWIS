from django.urls import path
from account.views import UserRegistrationView


urlpatterns = [
    path('registration/', UserRegistrationView.as_view(), name='registration')
]
