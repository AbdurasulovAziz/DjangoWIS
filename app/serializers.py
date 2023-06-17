from django.core.mail import EmailMessage
from rest_framework import serializers

from app import models


class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Food
        fields = "__all__"


class DrinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Drink
        fields = "__all__"


class SauceSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Sauce
        fields = "__all__"


class DessertSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Dessert
        fields = "__all__"


class BoxMixSerializer(serializers.ModelSerializer):
    box_drink = DrinkSerializer()
    box_food = serializers.StringRelatedField(source='box_food.name')

    class Meta:
        model = models.BoxMix
        fields = [
            "id",
            "name",
            "price",
            "description",
            "on_stop",
            "box_food",
            "box_drink",
            "box_sauce",
            "box_dessert",
        ]

    def to_representation(self, instance: models.BoxMix):
        obj = super(BoxMixSerializer, self).to_representation(instance)
        obj["box_sauce"] = instance.box_sauce.name
        return obj


class CartItemAddSerializer(serializers.ModelSerializer):
    count = serializers.IntegerField()

    class Meta:
        model = models.OrderItem
        fields = ['id', 'count']
        read_only_fields = ('id',)


class CartItemSerializer(serializers.ModelSerializer):
    price = serializers.IntegerField(read_only=True)

    class Meta:
        model = models.OrderItem
        fields = ["id", "dish", "count", "price"]
        read_only_fields = ('id', 'count', 'dish')

    def to_representation(self, instance: models.OrderItem):
        obj = super(CartItemSerializer, self).to_representation(instance)
        obj["dish"] = instance.dish.name
        obj["price"] = instance.dish.price
        return obj


class CartSerializer(serializers.ModelSerializer):
    user = serializers.CharField(read_only=True)
    items = CartItemSerializer(many=True, read_only=True)

    class Meta:
        model = models.Order
        fields = ["user", "status", "items"]

    def to_representation(self, instance: models.Order):
        obj = super(CartSerializer, self).to_representation(instance)
        obj["total_price"] = instance.get_total_price
        return obj

    def update(self, instance: models.Order, validated_data):
        instance = super().update(instance, validated_data)
        instance.status = "Sent"

        EmailMessage(
            "UserCode",
            f"Ваш заказ будет доставлен в течении 15 минут",
            to=[instance.user.email],
        ).send()

        instance.save()

        return instance
