from django.urls import path
from account.views import UserRegistrationVerifyView, UserRegistrationView


urlpatterns = [
    path('registration/', UserRegistrationView.as_view(), name='registration'),
    path('verify/<str:email>/<str:activation_key>', UserRegistrationVerifyView.as_view(), name='verify'),
]
