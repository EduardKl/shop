from django.urls import path

from .views import *


app_name = 'catalog'
urlpatterns = [
    path('<slug:category_slug>/<slug:product_slug>/', ProductDetail.as_view(), name='product_detail')
]