from django.contrib.auth import get_user_model
from django.core.mail import EmailMessage
from rest_framework import serializers, status
from rest_framework.response import Response

from WISDjango import settings
from WISDjango.redis import RedisDB
from account.models import Profile


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(style={"input_type": "password"})

    class Meta:
        model = get_user_model()
        fields = ["email", "password"]


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ["phone", "birth_day", "region"]


class UserDetailSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer()
    is_staff = serializers.BooleanField(read_only=True)
    is_verified = serializers.BooleanField(read_only=True)
    email = serializers.EmailField(read_only=True)

    class Meta:
        model = get_user_model()
        fields = [
            "email",
            "first_name",
            "last_name",
            "is_staff",
            "is_verified",
            "profile",
        ]

    def update(self, instance, validated_date):
        profile_data = validated_date.pop("profile", None)
        instance = super().update(instance, validated_date)

        if profile_data:
            profile_serializer = ProfileSerializer(instance.profile, data=profile_data)
            if profile_serializer.is_valid():
                profile_serializer.save()

        return instance
