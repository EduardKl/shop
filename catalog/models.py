from django.db import models
from django.urls import reverse

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=200, db_index=True, verbose_name='Наименование')
    slug = models.SlugField(max_length=200, db_index=True, unique=True, verbose_name='Псевдоним')
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True, related_name='product', verbose_name='Категория')
    image = models.FileField(upload_to='products/%Y/%m/%d', blank=True, verbose_name='Изображение')
    description = models.TextField(blank=True, verbose_name='Описание')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    stock = models.PositiveIntegerField(verbose_name='На складе')
    available = models.BooleanField(default=True, verbose_name='Размещён')
    updated = models.DateTimeField(auto_now=True, verbose_name='Обновлён')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Создан')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('catalog:product_detail', kwargs={'product_slug': self.slug})

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ('name',)

        index_together = (('id', 'slug'),)


class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True, verbose_name='Наименование')
    slug = models.SlugField(max_length=200, db_index=True, unique=True, verbose_name='Псевдоним')
    parent_cat = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True, related_name='children', verbose_name='Родительская категория')
    child_cat = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True, related_name='parents', verbose_name='Дочерняя категория')


    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('catalog:product_list_by_category', kwargs={'category_slug': self.slug})
    class Meta:
        verbose_name = 'Категория товара'
        verbose_name_plural = 'Категории товаров'
        ordering = ('name',)