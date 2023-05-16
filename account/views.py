from django.contrib.auth import get_user_model, views
from django.core.mail import EmailMessage

from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.views import View
from django.urls import reverse


from WISDjango.redis import RedisDB
from account.forms import RegistrationForm


# Create your views here.

class UserRegistrationView(View):

    UserModel = get_user_model()
    template_path = 'account/registration.html'

    def get(self, request, *args, **kwargs):
        form = RegistrationForm()
        return render(request, self.template_path, {'form': form})

    def post(self, request, *args, **kwargs):
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            code = RedisDB.create_user_registration_code(user.email)
            if EmailMessage("UserCode",
                            f"http://127.0.0.1:8000/account/verify/{user.email}/{code}",
                            to=["azizabdurasulov2002@gmail.com"]
                            ).send():

                return render(request, 'account/registration_confirm.html')

        else:
            form = RegistrationForm()
        return render(request, self.template_path, {'form': form})


class UserRegistrationVerifyView(View):

    UserModel = get_user_model()

    def get(self, request, *args, **kwargs):
        user = self.UserModel.objects.get(email=self.kwargs.get('email'))

        if RedisDB.check_user_registration_code(
                user.email,
                self.kwargs.get('activation_key')
        ):
            self.UserModel.objects.filter(email=user.email).update(if_verified=True)
            return HttpResponseRedirect(reverse('login'))

        else:
            return HttpResponse('<h1>Ссылка не действительна</h1>')


# class UserPasswordResetView(views.PasswordResetView):
#     template_name = 'registration/password_reset_email.html'