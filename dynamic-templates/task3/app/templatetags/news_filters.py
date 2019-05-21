from datetime import datetime
from django import template


register = template.Library()


@register.filter
def format_date(value):
    date = datetime.fromtimestamp(value)
    current_date = datetime.now()
    delta_minutes = (current_date - date).seconds // 60

    if delta_minutes <= 10:
        value = 'Только что'
    elif 10 < delta_minutes <= 1440:
        value = f'{delta_minutes // 60} часов назад'
    else:
        value = date

    return value


@register.filter
def format_score(value):
    if value:  
        score_count = int(value)

        if score_count < -5:
            value = 'все плохо'
        elif -5 <= score_count <= 5:
            value = 'нейтрально'
        else:
            value = 'хорошо'

    return value


@register.filter
def format_num_comments(value):
    comments_count = int(value)
    
    if comments_count == 0:
        value = 'Оставьте комментарий'
    elif comments_count > 50:
        value = '50+'

    return value

@register.filter
def format_selftext(value, arg):
    if value:
        filter = int(arg)
        words = value.split()

        value = f'{" ".join(words[:filter])} ... {" ".join(words[-filter:])}'

    return value

