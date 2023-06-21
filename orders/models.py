from django.db import models
from catalog.models import Product


# Create your models here.
class Order(models.Model):
    first_name = models.CharField(max_length=50, verbose_name='имя')
    last_name = models.CharField(max_length=50, verbose_name='Фамилия')
    email = models.EmailField(verbose_name='Электронная почта')
    city = models.CharField(max_length=100, verbose_name='Город')
    address = models.CharField(max_length=250, verbose_name='Почтовый адрес')
    postal_code = models.CharField(max_length=20, verbose_name='Почтовый индекс')
    updated = models.DateTimeField(auto_now=True, verbose_name='Обновлён')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Создан')
    paid = models.BooleanField(default=False, verbose_name='Оплачен')

    def __str__(self) -> str:
        return f'Заказ {self.id}'
    
    def get_total_cost(self):
        return sum(item.get_cost() for item in self.list_items.all())
    
    
    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
        ordering = ['-created']
        indexes = [
            models.Index(fields=['-created'])
        ]


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='list_items', on_delete=models.CASCADE, verbose_name='Т=Заказ')
    product = models.ForeignKey(Product, related_name='order_products', on_delete=models.CASCADE, verbose_name='Товар')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    quantity = models.PositiveBigIntegerField(default=1, verbose_name='Количество')

    def __str__(self) -> str:
        return f'Товар {self.id} заказа {self.order}'
    
    def get_cost(self):
        return self.price * self.quantity
    

    class Meta:
        verbose_name = 'Список товаров'
        verbose_name_plural = 'Список товаров'