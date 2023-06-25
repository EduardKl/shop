from typing import Any, Dict
from django.db.models.query import QuerySet
from django.db.models import Q
from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import *
from cart.forms import CartAddProductForm

# Create your views here.
class MainCatalogPage(ListView):
    model = Product
    template_name = 'catalog/main_catalog.html'
    context_object_name = 'products'
    extra_context = {'title': 'Главная'}

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'categories': Category.objects.all()})
        return context
    
    
class ProductsByCategory(ListView):
    """Класс-представления для отображения списка товаров выбранной категории."""
    model = Product
    template_name = 'catalog/main_catalog.html'
    context_object_name = 'products'
    slug_url_kwarg = 'category_slug'
    
    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        """Функция собирает контекст для шаблона."""
        context = super().get_context_data(**kwargs)
        
        category = Category.objects.get(slug=self.kwargs['category_slug'])
        context.update({
            'title': category.name,
            'categories': Category.objects.all()
        })

        return context
    
    def get_queryset(self) -> QuerySet[Any]:
        """
        Функция корректирует выборку из БД.
        В шаблон, в переменную products, передаются строки, которые либо относятся к выбранной категории, либо их категория является дочерней к выбранной.
        """
        return Product.objects.filter(Q(category__slug=self.kwargs['category_slug']) | Q(category__parent_cat__slug=self.kwargs['category_slug']))


class ProductDetail(DetailView):
    """Класс-представления для отображения детальной информации о товаре."""
    model = Product
    template_name = 'catalog/product_detail.html'
    context_object_name = 'product'
    extra_context = {'title': 'Товар'}

    slug_url_kwarg = 'product_slug'

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['cart_product_form'] = CartAddProductForm()
        return context
