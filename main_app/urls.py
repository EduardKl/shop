from django.urls import path

from .views import *


app_name = 'main_app'
urlpatterns = [
    path('', MainPage, name='main')
]