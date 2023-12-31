from django.db import models

from users.models import User

from utils import NULLABLE


class Category(models.Model):
    name = models.CharField(max_length=200, verbose_name='Наименование')
    description = models.TextField(verbose_name='Описание')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Product(models.Model):
    name = models.CharField(max_length=200, verbose_name='Наименование')
    description = models.TextField(verbose_name='Описание')
    image = models.ImageField(upload_to='products/', **NULLABLE, verbose_name='Изображение')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    price = models.PositiveIntegerField(verbose_name='Цена')
    date_created = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    user_created = models.ForeignKey(User, on_delete=models.SET(None), **NULLABLE, verbose_name='Автор')
    date_last_modified = models.DateTimeField(auto_now=True, verbose_name='Дата последнего изменения')

    def __str__(self):
        return f'{self.name} ({self.category})'

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


class Version(models.Model):
    name = models.CharField(max_length=200, verbose_name='Название версии')
    nomer = models.PositiveIntegerField(verbose_name='Номер версии')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Продукт')
    is_actual_version = models.BooleanField(default=False, verbose_name='Признак актуальной версии')


    def __str__(self):
        return f'{self.product} - {self.name}'

    class Meta:
        verbose_name = 'Версия'
        verbose_name_plural = 'Версии'