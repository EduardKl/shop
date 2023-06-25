from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.views.decorators.http import require_POST

from .cart import Cart
from .forms import CartAddProductForm
from catalog.models import Product

# Create your views here.
@require_POST
def card_add(request, product_slug):
    cart = Cart(request)
    product = get_object_or_404(Product, slug=product_slug)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        form_data = form.cleaned_data
        cart.add(product=product,
                 quantity=form_data['quantity'],
                 override_quantity=form_data['override'])
    return redirect('cart:detail')

@require_POST
def card_remove(request, product_slug):
    cart = Cart(request)
    product = get_object_or_404(Product, slug=product_slug)
    cart.remove(product.id)
    return redirect('cart:detail')

def cart_detail(request):
    cart = Cart(request)
    for item in cart:
        item['update_quantity_form'] = CartAddProductForm(initial={
            'quantity': item['quantity'],
            'override': True
        })
    return render(request, 'cart/cart_detail.html', {'title': 'Корзина', 'cart': cart})
    # return render('main_app/main.html', {'title': 'Из представления корзины.'})
    # return HttpResponse('Содержимое корзины.')