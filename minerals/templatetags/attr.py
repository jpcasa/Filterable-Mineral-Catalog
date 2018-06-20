"""template tags and filters for the minerals app"""
from django import template

register = template.Library()

@register.filter
def titlize(string):
    """Returns string without underscores"""
    return string.replace('_', ' ')
