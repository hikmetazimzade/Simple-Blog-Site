from django import template
import html

register = template.Library()

@register.filter
def decode_entities(value):
    return html.unescape(value)