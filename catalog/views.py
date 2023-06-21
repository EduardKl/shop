from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import *
from cart.forms import CartAddProductForm

# Create your views here.
class ProductDetail(DetailView):
    model = Product
    template_name = 'catalog/product_detail.html'
    context_object_name = 'product'
    extra_context = {'title': 'Товар'}

    slug_url_kwarg = 'product_slug'

    def get_context_data(self, *, objrvt_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cart_product_form'] = CartAddProductForm()
        return context
