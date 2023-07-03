from django.shortcuts import render
from django.core.mail import send_mail

from shop_site import settings
from .models import OrderItem
from .forms import OrderCreateForm
from .tasks import order_created
from cart.cart import Cart


# Create your views here.
def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            cart_items = []
            for item in cart:
                product = item['product']
                price = item['price']
                quantity = item['quantity']


                cart_items.append({'name': product.name, 'total_price': item['total_price'], 'price': price, 'quantity': quantity})
                OrderItem.objects.create(
                    order = order,
                    product = product,
                    price = price,
                    quantity = quantity
                )
            cart.clear()
            # order_created.delay(order.id)
            
            send_mail(f'Заказ {order.id} оформлен.',
                      f'Заказ {order.id} на товары {cart_items} оформлен.',
                      settings.EMAIL_HOST_USER,
                      [order.email], 
                      fail_silently=False
            )
            return render(request, 'orders/order_created.html', {'order': order})
    else:
        form = OrderCreateForm()
        return render(request, 'orders/order_create.html', {'cart': cart, 'form': form})