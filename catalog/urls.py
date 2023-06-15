from django.urls import path

from .views import *


app_name = 'catalog'
urlpatterns = [
    path('', MainPage.as_view(), name='main')
]