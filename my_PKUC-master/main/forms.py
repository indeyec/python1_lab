from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from polls.models import *
from polls.models import UserProfile

class UserForm(ModelForm):
    class Meta:
        model = UserProfile
        fields = '__all__'
        exclude = ['user']


class ChangeUserInfoForm(forms.ModelForm):
    email = forms.EmailField(required=True,
                             label='Адрес электронной почты')

    class Meta:
        model = UserProfile
        fields = ('user', 'image')