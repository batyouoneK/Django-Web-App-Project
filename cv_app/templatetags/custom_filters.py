from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()

@register.filter
@stringfilter
def split_string(value, delimiter=','):
    """
    Split a string by delimiter and return a list.
    
    Usage: 
    {{ value|split_string:"," }}
    
    Default delimiter is comma.
    """
    return value.split(delimiter)

@register.filter
@stringfilter
def strip(value):
    """
    Strip leading and trailing whitespace.
    
    Usage:
    {{ value|strip }}
    """
    return value.strip()