from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, DetailView

from app.models import Food, Drink, Sauce, Dessert, BoxMix


class DishAbstractPage(ListView):
    template_name = "app/menu.html"
    context_object_name = "data"


class DishDetailAbstractPage(DetailView):
    template_name = "app/menu-detail.html"
    context_object_name = "data"


class FoodPage(DishAbstractPage):
    model = Food

    def get_queryset(self):
        queryset = self.model.objects.values(
            "name", "price", "description", "on_stop", "category", "spicy"
        )

        return queryset


class FoodDetailPage(DishDetailAbstractPage):
    model = Food

    def get_queryset(self):
        queryset = self.model.objects.filter(id=self.kwargs['pk']).values(
            "name", "price", "description", "on_stop", "category", "spicy"
        )

        return queryset


class DrinkPage(DishAbstractPage):
    model = Drink

    def get_queryset(self):
        queryset = self.model.objects.values(
            "name", "price", "description", "on_stop", "category", "liter"
        )

        return queryset


class DrinkDetailPage(DishDetailAbstractPage):
    model = Drink

    def get_queryset(self):
        queryset = self.model.objects.filter(id=self.kwargs['pk']).values(
            "name", "price", "description", "on_stop", "category", "liter"
        )

        return queryset


class SaucePage(DishAbstractPage):
    model = Sauce

    def get_queryset(self):
        queryset = self.model.objects.values(
            "name", "price", "description", "on_stop"
        )

        return queryset


class SauceDetailPage(DishDetailAbstractPage):
    model = Sauce

    def get_queryset(self):
        queryset = self.model.objects.filter(id=self.kwargs['pk']).values(
            "name", "price", "description", "on_stop"
        )

        return queryset


class DessertPage(DishAbstractPage):
    model = Dessert

    def get_queryset(self):
        queryset = self.model.objects.values(
            "name", "price", "description", "on_stop"
        )

        return queryset


class DessertDetailPage(DishDetailAbstractPage):
    model = Dessert

    def get_queryset(self):
        queryset = self.model.objects.filter(id=self.kwargs['pk']).values(
            "name", "price", "description", "on_stop"
        )

        return queryset


class BoxMixPage(DishAbstractPage):
    model = BoxMix

    def get_queryset(self):
        queryset = self.model.objects.values(
            "name", "price", "description", "on_stop", "box_food__spicy"
        )

        return queryset


class BoxMixDetailPage(DishDetailAbstractPage):
    model = BoxMix

    def get_queryset(self):
        queryset = self.model.objects.filter(id=self.kwargs['pk']).values(
            "name", "price", "description", "on_stop", "box_food__spicy"
        )

        return queryset
