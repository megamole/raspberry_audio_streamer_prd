from django import template
from django.utils.text import Truncator

register = template.Library()

@register.filter("custom_truncator")
def custom_truncator(value, max_len, trunc_chars=True):
    truncator = Truncator(value)
    return truncator.chars(max_len) if trunc_chars else truncator.words(max_len)