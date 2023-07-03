from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class RegisterUserForm(UserCreationForm):
    first_name = forms.CharField(label='Имя', widget=forms.TextInput(attrs={'class': 'register-form__first-name'}))
    last_name = forms.CharField(label='Фамилия', widget=forms.TextInput(attrs={'class': 'register-form__last-name'}))
    email = forms.EmailField(label='Электронная почта', widget=forms.EmailInput(attrs={'class': 'register-form__email'}))
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'register-form__username'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'register-form__password'}))
    password2 = forms.CharField(label='Потвор пароля', widget=forms.PasswordInput(attrs={'class': 'register-form__password'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'auth-form__username'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'auth-form__password'}))