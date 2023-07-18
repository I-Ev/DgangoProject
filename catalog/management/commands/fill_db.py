
import json

from django.core.management import BaseCommand

from catalog.models import Product, Category


class Command(BaseCommand):

    def handle(self, *args, **options):
        Category.objects.all().delete()
        Product.objects.all().delete()

        with open('data.json', 'r', encoding='utf-16') as f:
            data = json.load(f)

        categories_for_create = []
        products_for_create = []

        for i in data:
            if i['model'] == 'catalog.category':
                category = Category(
                    pk=i['pk'],
                    name=i['fields']['name'],
                    description=i['fields']['description'],
                    created_at=i['fields']['created_at']
                )
                categories_for_create.append(category)
            elif i['model'] == 'catalog.product':
                product = Product(
                    pk=i['pk'],
                    name=i['fields']['name'],
                    description=i['fields']['description'],
                    image=i['fields']['image'],
                    category_id=i['fields']['category'],
                    price=i['fields']['price']
                )
                products_for_create.append(product)

        Category.objects.bulk_create(categories_for_create)
        Product.objects.bulk_create(products_for_create)
