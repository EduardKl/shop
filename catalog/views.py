from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import *


# Create your views here.
class MainPage(ListView):
    model = Product
    template_name = 'catalog/main.html'
    context_object_name = 'products'
    extra_context = {'title': 'Главная'}

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'categories': Category.objects.all()})
        return context

class ProductDetail(DetailView):
    model = Product
    template_name = 'catalog/product_detail.html'
    context_object_name = 'product'
    extra_context = {'title': 'Товар'}

    slug_url_kwarg = 'product_slug'
