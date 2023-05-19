from django.urls import path
from account import views

urlpatterns = [
    path('registration/', views.UserRegistrationView.as_view(), name='registration'),
    path('verify/<str:email>/<str:activation_key>', views.UserRegistrationVerifyView.as_view(), name='verify'),
    path('profile/<str:email>/', views.UserProfileView.as_view(), name='profile')
]
