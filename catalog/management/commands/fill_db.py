import json

from django.core.management import BaseCommand

from catalog.models import Product, Category


class Command(BaseCommand):

    def handle(self, *args, **options):
        Category.objects.all().delete()
        Product.objects.all().delete()
        with open('data.json', 'r', encoding='UTF-8') as f:
            data = json.load(f, encoding='utf-8')

            categories_for_create=[]
            products_for_create=[]
            for i in data:
                categories_for_create.append(Category(**i))
                products_for_create.append(Product(**i))

            Category.objects.bulk_create(categories_for_create)
            Product.objects.bulk_create(products_for_create)