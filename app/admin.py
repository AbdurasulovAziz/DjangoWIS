from django.contrib import admin
from django.db.models import F
from django.http import HttpResponseRedirect
from django.urls import path, reverse

from app import models
from app.models_actions import put_on_stop_list, remove_from_stop_list


# Register your models here.


def go_next_instance(request, object_id):
    next_object_id = models.Food.objects.filter(id__gt=object_id).first()
    if next_object_id:
        return HttpResponseRedirect(
            reverse("admin:app_food_change", args=(next_object_id.id,))
        )
    else:
        return HttpResponseRedirect(reverse("admin:app_food_changelist"))


@admin.register(models.Food)
class FoodAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "price",
        "category",
        "spicy",
        "on_stop",
    )
    search_fields = ("name",)
    list_filter = (
        "category",
        "spicy",
        "on_stop",
    )
    actions = (
        put_on_stop_list,
        remove_from_stop_list,
    )
    ordering = ("id",)
    change_form_template = "admin/custom_change_form.html"

    def get_urls(self):
        urls = super().get_urls()
        extra_urls = [
            path("<int:object_id>/next/", go_next_instance, name="app_food_next")
        ]

        return extra_urls + urls


class DrinkAdminFilter(admin.SimpleListFilter):
    title = "Filters"
    parameter_name = "filter"

    def lookups(self, request, model_admin):
        return (
            ("Hot", "Hot Drinks"),
            ("Cold", "Cold Drinks"),
        )

    def queryset(self, request, queryset):
        values = ("Hot", "Cold")
        value = self.value()
        if value not in values:
            raise AttributeError
        return queryset.filter(category=value)


@admin.register(models.Drink)
class DrinkAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "price",
        "liter",
        "category",
        "on_stop",
    )
    search_fields = ("name",)
    list_filter = (DrinkAdminFilter,)
    actions = (
        put_on_stop_list,
        remove_from_stop_list,
    )


@admin.register(models.Sauce)
class SauceAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "price",
        "on_stop",
    )
    search_fields = ("name",)
    actions = (
        put_on_stop_list,
        remove_from_stop_list,
    )


@admin.register(models.Dessert)
class DessertAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "price",
        "on_stop",
    )
    search_fields = ("name",)
    actions = (
        put_on_stop_list,
        remove_from_stop_list,
    )


@admin.register(models.BoxMix)
class BoxMixAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "box_food",
        "box_drink",
        "box_sauce",
        "box_dessert",
        "price",
        "on_stop",
    )
    actions = (
        put_on_stop_list,
        remove_from_stop_list,
    )
    readonly_fields = ("get_price_with_sale",)
    search_fields = ("name", "food")


class OrderItemTabular(admin.TabularInline):
    model = models.OrderItem
    extra = 1
    readonly_fields = (
        "get_dish_price",
        "get_total_price",
    )


@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    inlines = [OrderItemTabular]
