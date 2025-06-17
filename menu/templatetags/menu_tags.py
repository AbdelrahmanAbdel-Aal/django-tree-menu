from django import template
from django.utils.safestring import mark_safe
from menu.models import Menu, MenuItem
from django.urls import resolve

register = template.Library()

@register.inclusion_tag("menu/menu.html", takes_context=True)
def draw_menu(context, menu_name):
    request = context["request"]
    current_path = request.path

    try:
        menu = Menu.objects.get(name=menu_name)
    except Menu.DoesNotExist:
        return {"menu_items": []}

    # كل العناصر المرتبطة بالقائمة
    items = MenuItem.objects.filter(menu=menu).select_related("parent")
    items_by_id = {item.id: item for item in items}

    # بناء هيكل الشجرة
    for item in items:
        item.childrenn = []
    for item in items:
        if item.parent_id:
            items_by_id[item.parent_id].childrenn.append(item)



    # حدد العنصر الحالي في الشجرة حسب الرابط
    active_ids = set()
    for item in items:
        if item.get_url() == current_path:
            current = item
            while current:
                active_ids.add(current.id)
                current = current.parent
            break

    # العناصر الجذرية (اللي مالهاش parent)
    root_items = [item for item in items if item.parent is None]

    return {
        "menu_items": root_items,
        "active_ids": active_ids,
        "request": request,
    }
