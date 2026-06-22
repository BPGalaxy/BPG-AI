from django import template

register = template.Library()

@register.filter
def first_char(value):
    """Returns the first character of a string."""
    if value:
        return value[0]
    return ''

@register.filter
def get_item(dictionary, key):
    """Gets an item from a dictionary using a variable key."""
    return dictionary.get(key)
