from django.template import Library

register = Library()

@register.filter
def mediapath(path):
    return "/media/" + path


