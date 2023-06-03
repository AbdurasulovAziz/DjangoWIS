from django import template
from django.urls import reverse

register = template.Library()


@register.filter(name="get_class_name")
def get_class_name(model):
    return model._meta.model_name


@register.simple_tag
def redirect_to_dish_detail_url(dish_name, pk):
    return reverse(f"{dish_name}-detail", args=[pk])


@register.simple_tag
def multiply(value1, value2):
    return value1 * value2


@register.simple_tag
def get_total_price(object):
    count = [item.dish.price * item.count for item in object]
    return sum(count)


@register.simple_tag
def get_all(value):
    return value.orderitem_set.all()
