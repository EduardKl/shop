from django import template

from catalog.models import Category


register = template.Library()

@register.inclusion_tag('catalog/user_tags_templates/cat_menu.html')
def show_cat_menu():
    nav_menu = Category.objects.all()
    context = {'nav_menu': nav_menu}
    return context