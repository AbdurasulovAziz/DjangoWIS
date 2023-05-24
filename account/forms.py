from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

from account.models import Profile


class RegistrationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ('email',)


class RegistrationCodeVerifyForm(forms.Form):
    code = forms.IntegerField()


class UserProfileForm(forms.ModelForm):
    phone = forms.CharField(required=None)
    birth_day = forms.DateField(required=None)
    region = forms.CharField(required=None)

    class Meta:
        model = get_user_model()
        fields = ('first_name', 'last_name', 'phone', 'birth_day', 'region')

    def save(self, commit=True):
        instance = super().save(commit=False)

        profile = instance.profile
        profile.phone = self.cleaned_data['phone']
        profile.birth_day = self.cleaned_data['birth_day']
        profile.region = self.cleaned_data['region']
        profile.save()



