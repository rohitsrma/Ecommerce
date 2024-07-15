from typing import Any
from django.forms import ModelForm
from django import forms
from accounts.models import User

class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('email', 'password')
    