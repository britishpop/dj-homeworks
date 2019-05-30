from django import template


register = template.Library()


@register.filter
def bool_replace(value):
    if isinstance (value, bool):
        value = 'Да' if value else 'Нет' 

    return value


