from django.urls import path
from app.views import HomePage


urlpatterns = [
    path('home', HomePage.as_view(), name='home'),
]
