from decimal import Decimal
from shop_site import settings
from catalog.models import Product


class Cart:
    def __init__(self, request):
        self.session = request.session
        self.cart = self.session.get(settings.CART_SESSION_ID)
        if not self.cart:
            self.cart = self.session[settings.CART_SESSION_ID] = {}
    def __len__(self):
        """Функция возвращает общее количество товаров в корзине."""
        return sum([item['quantity'] for item in self.cart.values()])
    def __iter__(self):
        products_id = self.cart.keys()
        products = Product.objects.filter(id__in=products_id)
        for product in products:
            self.cart[str(product.id)]['product'] = product

        for item in self.cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item

    def get_total_price(self):
        """Функция возвращает общую стоимость товаров в карзине."""
        return sum([Decimal(item['price']) * item['quantity'] for item in self.cart.values()])

    def add(self, product, quantity = 1, override_quantity = False):
        product_id = str(product.id)

        if product_id not in self.cart:
            self.cart.update({product_id: {
                'quantity': 0,
                'price': str(product.price)
            }})

        if override_quantity:
            self.cart[product_id]['quantity'] = quantity
        else:
            self.cart[product_id]['quantity'] += quantity

        self.save()

    def save(self):
        self.session.modified = True

    def remove(self, product_id):
        product_id = str(product_id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()
    
    def clear(self):
        del self.session[settings.CART_SESSION_ID]
        self.save()