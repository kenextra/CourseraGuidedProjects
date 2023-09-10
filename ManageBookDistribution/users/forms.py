from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class UserRegisterForm(UserCreationForm):
    # add email field to the form
    email = forms.EmailField(required=True)

    # nested namespace for configurations and keeps the configurations in one place
    class Meta:
        # model that will be affected
        model = User
        # fields that will be displayed in the form and in what order
        fields = ['username', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    # add email field to the form
    email = forms.EmailField()

    # nested namespace for configurations and keeps the configurations in one place
    class Meta:
        # model that will be affected
        model = User
        # fields that will be displayed in the form and in what order
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']