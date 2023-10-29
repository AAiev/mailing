from django import template
from django.conf import settings

register = template.Library()


@register.simple_tag()
def media_file(shot_path):
    if shot_path:
        return f'{settings.MEDIA_URL}{shot_path}'
    else:
        return '#'