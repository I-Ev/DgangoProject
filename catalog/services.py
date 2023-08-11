from django.core.cache import cache
from catalog.models import Category
from config import settings


def get_cached_categories_list():
    cache_key = 'category_list'

    if settings.CACHE_ENABLE:
        category_list = cache.get(cache_key)

        if category_list is None:
            category_list = Category.objects.all()
            cache.set(cache_key, category_list, 60 * 60)  # Кэширование на 1 час
    else:
        category_list = Category.objects.all()
        cache.set(cache_key, category_list, 60 * 60)  # Кэширование на 1 час
    return category_list
