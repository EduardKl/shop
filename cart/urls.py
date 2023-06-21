from django.urls import path

from .views import *


app_name = 'cart'
urlpatterns = [
    path('', cart_detail, name='detail'),
    path('add/<slug:product_slug>', card_add, name='add'),
    path('remove/<slug:product_slug>', card_remove, name='remove')
]