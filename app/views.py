# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

from .forms import RegistrationForm
from WISDjango.settings import AUTH_USER_MODEL
from .models import CustomUser


class UserRegistrationView(View):

    template_path = 'registration/registration.html'

    def get(self, request, *args, **kwargs):
        form = RegistrationForm()
        return render(request, self.template_path, {'form': form})


    def post(self, request, *args, **kwargs):
        form = RegistrationForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            password_confirm = form.cleaned_data.get('password_confirm')
            if password == password_confirm:
                CustomUser.objects.create_user(email, password)
                return HttpResponse('<h1>Зарегались</h1>')
        else:
            form = RegistrationForm()
        return render(request, self.template_path, {'form': form})


