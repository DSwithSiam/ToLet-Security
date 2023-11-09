from django import forms
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField, PasswordChangeForm
from django.utils.translation import gettext, gettext_lazy as _


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(
        attrs={'autofocus': True, 'class': 'form-control', 'placeholder': 'Username'}))
    password = forms.CharField(label=_('Password'), strip=False, widget=forms.PasswordInput(
        attrs={'autocomplete': True, 'class': 'form-control', 'placeholder': 'Password'}))


class ChangePasswordForm(PasswordChangeForm):
    old_password = forms.CharField(label=_('Current Password'), strip=False, widget=forms.PasswordInput(
        attrs={'autocomplete': True, 'class': 'form-control', 'placeholder': 'Current Password'}))
    new_password1 = forms.CharField(label=_('New Password'), strip=False, widget=forms.PasswordInput(
        attrs={'autocomplete': True, 'class': 'form-control', 'placeholder': 'New Password'}))
    new_password2 = forms.CharField(label=_('Confirm Password'), strip=False, widget=forms.PasswordInput(
        attrs={'autocomplete': True, 'class': 'form-control', 'placeholder': 'Confirm Password'}))
