from django import template
from news.models import Categories


register = template.Library()

@register.simple_tag()
def get_categories():
    return Categories.objects.all()