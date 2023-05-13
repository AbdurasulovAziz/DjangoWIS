from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django.shortcuts import render
from django.views import View

from WISDjango.redis import RedisDB
from account.forms import RegistrationForm
# Create your views here.


class UserRegistrationView(View):

    UserModel = get_user_model()
    template_path = 'registration/registration.html'

    def get(self, request, *args, **kwargs):
        form = RegistrationForm()
        return render(request, self.template_path, {'form': form})

    def post(self, request, *args, **kwargs):
        form = RegistrationForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password1 = form.cleaned_data.get('password1')
            password2 = form.cleaned_data.get('password2')

            if password1 == password2:
                code = RedisDB.create_user_registration_code(email=email)
                self.UserModel.objects.create_user(email, password1)
                send_mail(
                    "UserCode",
                    f"{code}",
                    "azizabdurasulov2002@gmail.com",
                    ["azizabdurasulov2002@gmail.com"],
                    fail_silently=False,
                )

                return render(request, 'registration/confirm_registration.html')

        else:
            form = RegistrationForm()
        return render(request, self.template_path, {'form': form})

