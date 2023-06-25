from django.shortcuts import render

# Create your views here.
def MainPage(request):
    return render(request, 'main_app/main.html', {'title': 'Главная'})
    
def pageNotFound(request, exception):
    return render('main_app/404.html', {'title': 'Такой страницы нет.'})