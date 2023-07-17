import json

from django.core.management import BaseCommand

from catalog.models import Product, Category


class Command(BaseCommand):

    def handle(self, *args, **options):
        Category.objects.all().delete()
        Product.objects.all().delete()
        with open('data.json', 'r', encoding='utf-16') as f:
            data = json.load(f)

            categories_for_create=[]
            products_for_create=[]
            for i in data:
                if i['model'] == 'catalog.category':
                    categories_for_create.append(Category(**i['fields']))
                elif i['model'] == 'catalog.product':
                    products_for_create.append(Product(**i['fields']))

            Category.objects.bulk_create(categories_for_create)
            Product.objects.bulk_create(products_for_create)