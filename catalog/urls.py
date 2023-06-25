from django.urls import path

from .views import *


app_name = 'catalog'
urlpatterns = [
    path('', MainCatalogPage.as_view(), name='main_catalog'),
    path('<slug:category_slug>/<slug:product_slug>/', ProductDetail.as_view(), name='product_detail'),
    path('product_list_by_category/<slug:category_slug>', ProductsByCategory.as_view(), name='product_list_by_category')
]