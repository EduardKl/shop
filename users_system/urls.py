from django.urls import path

from .views import RegisterUser, LoginUser, logout_user


app_name = 'users_system'
urlpatterns = [
    path('register/', RegisterUser.as_view(), name='register'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name="logout")
]