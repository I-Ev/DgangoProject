from django.template import Library

register = Library()

@register.filter
def mediapath(path):
    path_str = str(path)
    return "/media/" + path_str


@register.simple_tag
def mediapath(path):
    path_str = str(path)
    return "/media/" + path_str