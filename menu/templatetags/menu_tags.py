from django import template
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import get_object_or_404

from menu.models import Menu

register = template.Library()

@register.inclusion_tag('menus/menu.html', takes_context=True)
def draw_menu(context, name):
    menu = get_object_or_404(Menu, name=name, parent=None)
    request_url = context['request'].path
    context = {'menu_item': menu}
    try:
        current_menu_item = Menu.objects.get(url=request_url)
    except ObjectDoesNotExist:
        pass
    else:
        unwrapped_menu_items_id = current_menu_item.get_id() + [current_menu_item.id] # развернутые идентификаторы пунктов меню
        context['unwrapped_menu_items_id'] = unwrapped_menu_items_id
    return context

@register.inclusion_tag('menus/menu.html', takes_context=True)
def draw_submenu_item(context, item_id):
    menu_item = get_object_or_404(Menu, pk=item_id)
    l_context = {'menu_item': menu_item}
    if 'unwrapped_menu_items_id' in context:
        l_context['unwrapped_menu_items_id'] = context['unwrapped_menu_items_id']
    return l_context
