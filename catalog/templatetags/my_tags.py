from django.template import Library

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