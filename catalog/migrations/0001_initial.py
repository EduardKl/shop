# Generated by Django 4.2.2 on 2023-06-16 10:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=200, verbose_name='Наименование')),
                ('slug', models.SlugField(max_length=200, unique=True, verbose_name='Псевдоним')),
                ('child_cat', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='parents', to='catalog.category', verbose_name='Дочерняя категория')),
                ('parent_cat', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='catalog.category', verbose_name='Родительская категория')),
            ],
            options={
                'verbose_name': 'Категория товара',
                'verbose_name_plural': 'Категории товаров',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=200, verbose_name='Наименование')),
                ('slug', models.SlugField(max_length=200, unique=True, verbose_name='Псевдоним')),
                ('image', models.FileField(blank=True, upload_to='products/%Y/%m/%d', verbose_name='Изображение')),
                ('description', models.TextField(blank=True, verbose_name='Описание')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Цена')),
                ('stock', models.PositiveIntegerField(verbose_name='На складе')),
                ('available', models.BooleanField(default=True, verbose_name='Размещён')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Обновлён')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Создан')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='product', to='catalog.category', verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Товар',
                'verbose_name_plural': 'Товары',
                'ordering': ('name',),
                'index_together': {('id', 'slug')},
            },
        ),
    ]
