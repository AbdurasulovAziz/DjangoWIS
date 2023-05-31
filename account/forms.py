from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm


class RegistrationForm(UserCreationForm):
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={"style": "width:60%", "class": "py-1"})
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={"style": "width:60%", "class": "py-1"})
    )

    class Meta:
        model = get_user_model()
        fields = ("email", "password1", "password2")
        widgets = {
            "email": forms.TextInput(attrs={"style": "width:60%", "class": "py-1"})
        }


class UserProfileForm(forms.ModelForm):
    phone = forms.CharField(
        required=None,
        widget=forms.TextInput(attrs={"style": "width:60%", "class": "py-1"}),
    )
    birth_day = forms.DateField(
        required=None,
        widget=forms.TextInput(attrs={"style": "width:60%", "class": "py-1"}),
    )
    region = forms.CharField(
        required=None,
        widget=forms.TextInput(attrs={"style": "width:60%", "class": "py-1"}),
    )

    class Meta:
        model = get_user_model()
        fields = ("first_name", "last_name", "phone", "birth_day", "region")
        labels = {
            "first_name": "First name",
            "last_name": "Last name",
            "phone": "Phone",
            "birth_day": "Birth day",
            "region": "Region",
        }
        widgets = {
            "first_name": forms.TextInput(
                attrs={"style": "width:60%", "class": "py-1"}
            ),
            "last_name": forms.TextInput(attrs={"style": "width:60%", "class": "py-1"}),
        }

    def save(self, commit=True):
        instance = super().save(commit=False)

        profile = instance.profile
        profile.phone = self.cleaned_data["phone"]
        profile.birth_day = self.cleaned_data["birth_day"]
        profile.region = self.cleaned_data["region"]
        profile.save()
        instance.save()
