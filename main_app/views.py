from django.shortcuts import render
from django.views.generic import ListView

from catalog.models import Category, Product


# Create your views here.
class MainPage(ListView):
    model = Product
    template_name = 'main_app/main.html'
    context_object_name = 'products'
    extra_context = {'title': 'Главная'}

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'categories': Category.objects.all()})
        return context
    
def pageNotFound(request, exception):
    return render('main_app/404.html', {'title': 'Такой страницы нет.'})