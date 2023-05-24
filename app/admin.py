from django.contrib import admin
from django.db.models import F
from django.http import HttpResponseRedirect
from django.urls import path, reverse

from app import models
from app.models_actions import put_on_stop_list, remove_from_stop_list


# Register your models here.

def my_view(request, object_id): #TODO плохая запись
    next_object_id = models.Food.objects.filter(id__gt=object_id).first()
    if next_object_id:
        return HttpResponseRedirect(reverse('admin:app_food_change', args=(next_object_id.id,)))
    else:
        return HttpResponseRedirect(reverse('admin:app_food_changelist'))


@admin.register(models.Food)
class FoodAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'category', 'spicy', 'on_stop', )
    search_fields = ('name',)
    list_filter = ('category', 'spicy', 'on_stop',)
    actions = (put_on_stop_list, remove_from_stop_list,)
    ordering = ('id',)
    change_form_template = 'admin/custom_change_form.html'

    def get_urls(self):
        urls = super().get_urls()
        my_urls = [
            path('<int:object_id>/next/', my_view, name='app_food_next')
        ]

        return my_urls + urls


class DrinkAdminFilter(admin.SimpleListFilter):
    title = 'Filters'
    parameter_name = 'filter'

    def lookups(self, request, model_admin):
        return (
            ('Hot', 'Hot Drinks'),
            ('Cold', 'Cold Drinks'),
        )

    def queryset(self, request, queryset):
        if self.value() == 'Hot':
            return queryset.filter(
                category='Hot'
            )
        if self.value() == 'Cold':
            return queryset.filter(
                category='Cold'
            )


@admin.register(models.Drink)
class DrinkAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'liter', 'category', 'on_stop',)
    search_fields = ('name',)
    list_filter = (DrinkAdminFilter,)
    actions = (put_on_stop_list, remove_from_stop_list,)


@admin.register(models.Sauce)
class SauceAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'on_stop',)
    search_fields = ('name',)
    actions = (put_on_stop_list, remove_from_stop_list,)


@admin.register(models.Dessert)
class DessertAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'on_stop',)
    search_fields = ('name',)
    actions = (put_on_stop_list, remove_from_stop_list,)


@admin.register(models.BoxMix)
class BoxMixAdmin(admin.ModelAdmin):
    list_display = ('name', 'food', 'drink', 'sauce', 'dessert', 'on_stop', '_count_price')
    actions = (put_on_stop_list, remove_from_stop_list,)
    readonly_fields = ('_count_price',)
    search_fields = ('name', 'food')

    def _count_price(self, obj: models.BoxMix):
        return sum([
            obj.food.price,
            obj.drink.price,
            obj.sauce.price,
            obj.dessert.price
        ]) / 100 * 85

