from django.core.mail import EmailMessage
from django.http import HttpResponseRedirect, HttpResponseBadRequest
from django.shortcuts import render
from django.urls import reverse
from django.views import View
from django.views.generic import ListView, DetailView
from rest_framework.response import Response
from rest_framework.views import APIView

from app.models import Food, Drink, Sauce, Dessert, BoxMix, Order, Dish, OrderItem
from rest_framework import generics, mixins, status, permissions

from app.serializers import (
    FoodSerializer,
    DrinkSerializer,
    SauceSerializer,
    DessertSerializer,
    BoxMixSerializer,
    CartSerializer,
    CartItemSerializer, CartItemAddSerializer,
)


class FoodPage(generics.ListAPIView):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class FoodDetailPage(generics.RetrieveAPIView):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class DrinkPage(generics.ListAPIView):
    queryset = Drink.objects.all()
    serializer_class = FoodSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class DrinkDetailPage(generics.RetrieveAPIView):
    queryset = Drink.objects.all()
    serializer_class = DrinkSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class SaucePage(generics.ListAPIView):
    queryset = Sauce.objects.all()
    serializer_class = SauceSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class SauceDetailPage(generics.RetrieveAPIView):
    queryset = Sauce.objects.all()
    serializer_class = SauceSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class DessertPage(generics.ListAPIView):
    queryset = Dessert.objects.all()
    serializer_class = DessertSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class DessertDetailPage(generics.RetrieveAPIView):
    queryset = Dessert.objects.all()
    serializer_class = DessertSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class BoxMixPage(generics.ListAPIView):
    queryset = BoxMix.objects.all()
    serializer_class = BoxMixSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class BoxMixDetailPage(generics.RetrieveAPIView):
    queryset = BoxMix.objects.all()
    serializer_class = BoxMixSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class CartPageView(
    generics.GenericAPIView,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.RetrieveModelMixin,
):
    serializer_class = CartSerializer

    def get_object(self):
        order, created = Order.objects.get_or_create(
            user=self.request.user, status="Cart"
        )
        return order

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)


class CartItemView(
    generics.GenericAPIView,
    mixins.RetrieveModelMixin,
    mixins.DestroyModelMixin,
    mixins.UpdateModelMixin,
):
    serializer_class = CartItemSerializer

    def get_object(self):
        order_user, is_created = Order.objects.get_or_create(
            user=self.request.user, status="Cart"
        )
        return order_user.items.filter(id=self.kwargs.get("dish_id")).first()

    def get(self, request, *args, **kwargs):

        if not self.get_object():
            return Response(data={'Error': 'Object is not found'}, status=status.HTTP_404_NOT_FOUND)

        return self.retrieve(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class CartAddView(APIView):

    def post(self, request, dish_id, *args, **kwargs):
        serializer = CartItemAddSerializer(data=request.data)
        if serializer.is_valid():

            order, order_is_created = Order.objects.get_or_create(
                user=request.user, status="Cart"
            )
            order_item, item_is_created = order.items.get_or_create(dish_id=dish_id)
            order_item.count = order_item.count + serializer.validated_data.get("count")
            order_item.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


