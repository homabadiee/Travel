from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import PassengerUser


class CreateRegisterForm(UserCreationForm):
    class Meta:
        model = PassengerUser
        fields = ['phone', 'email', 'password1', 'password2']
