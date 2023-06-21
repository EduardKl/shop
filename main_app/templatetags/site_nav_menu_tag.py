from django import template

from catalog.models import Category


register = template.Library()

@register.inclusion_tag('main_app/user_tags_templates/nav_menu.html')
def show_nav_menu():
    nav_menu = Category.objects.all()
    context = {'nav_menu': nav_menu}
    return context