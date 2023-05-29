from django import template
from django.urls import reverse

register = template.Library()


@register.filter(name="get_class_name")
def get_class_name(model):
    return model._meta.model_name


@register.simple_tag
def dish_url(dish_name, pk):
    url = reverse(f"{dish_name}-detail", args=[pk])
    return url
