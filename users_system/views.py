from typing import Any, Dict
from django.shortcuts import render, redirect
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout
from django.urls import reverse_lazy

from .forms import RegisterUserForm, LoginUserForm



# Create your views here.
class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'users_system/register.html'
    success_url = reverse_lazy('users_system:login')
    
    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context.update({'title': 'Регистрация'})
        return context


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'users_system/login.html'

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context.update({'title': 'Авторизация'})
        return context
    
    def get_success_url(self) -> str:
        """Метод указывает, по какому адресу отправлять успешно авторизовавшегося пользователя."""
        return reverse_lazy('main_app:main')
    

def logout_user(request):
    logout(request)
    return redirect('users_system:login')


