# -*- coding: UTF-8 -*-
from django.template import Library
from django.template.defaultfilters import stringfilter
 
register = Library()
@register.filter(name='remove')
@stringfilter
def truncatehanzi(value, arg):
    """
    truncates a string after a certain number of words including
    alphanumeric and cjk characters.
 
    argument: number of words to truncate after.
    """
    from truncate_hanzi import truncate_hanzi
    try:
        length = int(arg)
    except ValueError: # invalid literal for int().
        return value # fail silently.
    return truncate_hanzi(value, length)
truncatehanzi.is_safe = True
 
register.filter('truncatehanzi', truncatehanzi)