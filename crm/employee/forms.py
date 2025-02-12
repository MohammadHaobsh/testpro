from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .models import Employee

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))

class RegisterForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))
    phone = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone'}))

    class Meta:
        model = Employee
        fields = ["username", "email", "phone", "password1", "password2"]
