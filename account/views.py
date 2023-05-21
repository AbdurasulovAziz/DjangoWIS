from django.contrib.auth import get_user_model, views
from django.core.mail import EmailMessage

from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.views import View
from django.urls import reverse

from django.views.generic import DetailView
from WISDjango import settings
from WISDjango.redis import RedisDB
from account.forms import RegistrationForm, UserProfileForm
from account.models import Profile


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
            if EmailMessage(
                    "UserCode",
                    f"{settings.EMAIL_VERIFICATION_URL}/{user.email}/{code}",
                    to=["azizabdurasulov2002@gmail.com"] #TODO поменять на user.email
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

        return HttpResponse('<h1>Ссылка не действительна</h1>')


class UserProfileAbstractView(DetailView):
    model = get_user_model()
    template_name = 'account/profile_detail.html'
    context_object_name = 'customuser'
    slug_field = 'email'
    slug_url_kwarg = 'email'


class UserProfileView(UserProfileAbstractView):
    pass


class UserProfileChangeView(UserProfileAbstractView):
    template_name = 'account/profile_detail_change.html'
    User = get_user_model()

    def get(self, request, *args, **kwargs):
        user_instance = self.User.objects.get(email=kwargs.get('email'))

        form = UserProfileForm(instance=user_instance)
        form.initial['phone'] = user_instance.profile.phone
        form.initial['birth_day'] = user_instance.profile.birth_day
        form.initial['region'] = user_instance.profile.region
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = UserProfileForm(
            request.POST,
            instance=self.User.objects.get(email=kwargs.get('email'))
        )
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('profile', args=[request.user.email]))



