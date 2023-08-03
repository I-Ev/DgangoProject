from django.template import Library

from catalog.models import Product, Version
from config import settings

register = Library()


@register.filter(name='mediapath')
def mediapath(value):
    if value:
        return f"{settings.MEDIA_URL}{value}"
    return "No image yet"


@register.simple_tag
def mediapath(path):
    path_str = str(path)
    return "/media/" + path_str


@register.simple_tag
@register.simple_tag
def get_current_version(product_id):
    try:
        product = Product.objects.get(id=product_id)
        current_version = product.version_set.get(is_actual_version=True)
        if current_version.nomer is not None:
            return f"v.{current_version.nomer}"
    except:
        return None
