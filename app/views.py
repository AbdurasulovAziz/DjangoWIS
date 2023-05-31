from django.core.mail import EmailMessage
from django.http import HttpResponseRedirect, HttpResponseBadRequest
from django.shortcuts import render
from django.urls import reverse
from django.views import View
from django.views.generic import ListView, DetailView

from app.forms import DishAddToCartForm
from app.models import Food, Drink, Sauce, Dessert, BoxMix, Order, OrderItem


class DishAbstractPage(ListView):
    template_name = "app/menu.html"
    context_object_name = "data"

    def get_context_data(self, *, object_list=None, **kwargs):
        queryset = super().get_context_data()
        queryset["form"] = DishAddToCartForm()
        return queryset


class DishDetailAbstractPage(DetailView):
    template_name = "app/menu-detail.html"
    context_object_name = "data"

    def get_queryset(self):
        queryset = self.model.objects.filter(id=self.kwargs["pk"]).values(
            "name", "price", "description", "on_stop", "category", "spicy"
        )

        return queryset


class FoodPage(DishAbstractPage):
    model = Food

    # def get_queryset(self):
    #     queryset = self.model.objects.values(
    #         "name", "price", "description", "on_stop", "category", "spicy"
    #     )
    #
    #     return queryset


class FoodDetailPage(DishDetailAbstractPage):
    model = Food


class DrinkPage(DishAbstractPage):
    model = Drink


class DrinkDetailPage(DishDetailAbstractPage):
    model = Drink


class SaucePage(DishAbstractPage):
    model = Sauce


class SauceDetailPage(DishDetailAbstractPage):
    model = Sauce


class DessertPage(DishAbstractPage):
    model = Dessert


class DessertDetailPage(DishDetailAbstractPage):
    model = Dessert


class BoxMixPage(DishAbstractPage):
    model = BoxMix


class BoxMixDetailPage(DishDetailAbstractPage):
    model = BoxMix


class CartPageView(View):
    def get(self, request, *args, **kwargs):
        queryset = Order.objects.filter(user=request.user, status="Cart").first()

        try:
            context = queryset.orderitem_set.all()
        except AttributeError:
            context = None

        return render(request, "app/cart.html", {"context": context})

    def post(self, request, *args, **kwargs):
        order = Order.objects.filter(user=request.user, status="Cart").first()
        if order is None:
            return HttpResponseBadRequest(
                "This view can not handle method".format(request.method), status=400
            )

        order.status = "Sent"
        order.save()
        if EmailMessage(
            "UserCode",
            f"Ваш заказ будет доставлен в течении 15 минут",
            to=["azizabdurasulov2002@gmail.com"],  # TODO поменять на user.email
        ).send():
            return HttpResponseRedirect(reverse("food-page"))


class CartAddView(View):
    def post(self, request, dish_id, *args, **kwargs):
        order, is_created = Order.objects.get_or_create(
            user=request.user, status="Cart"
        )
        order_item, is_created = order.orderitem_set.get_or_create(dish_id=dish_id)
        order_item.count = request.POST.get("count")
        order_item.save()

        return HttpResponseRedirect(reverse("food-page"))
