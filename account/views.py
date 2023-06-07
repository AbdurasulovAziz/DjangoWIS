from rest_framework import status
from django.contrib.auth import get_user_model, login
from django.core.mail import EmailMessage

from django.http import Http404
from django.shortcuts import get_object_or_404

from rest_framework.response import Response
from rest_framework.views import APIView

from WISDjango import settings
from WISDjango.redis import RedisDB
from account.serializers import UserSerializer, UserDetailSerializer


# Create your views here.


class UserRegistrationView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = get_user_model().objects.create_user(
                email=serializer.validated_data["email"],
                password=serializer.validated_data["password"],
            )
            code = RedisDB.create_user_registration_code(user.email)

            EmailMessage(
                "UserCode",
                f"{settings.EMAIL_VERIFICATION_URL}/{user.email}/{code}",
                to=[user.email],
            ).send()

            return Response(
                data={"email": user.email, "password": user.password},
                status=status.HTTP_200_OK,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserRegistrationVerifyView(APIView):
    UserModel = get_user_model()

    def get(self, request, *args, **kwargs):
        user = self.UserModel.objects.get(email=self.kwargs.get("email"))

        if RedisDB.check_user_registration_code(
            user.email, self.kwargs.get("activation_key")
        ):
            user.is_verified = True
            user.save()
            login(request, user)
            return Response(data={"total": "Success"}, status=status.HTTP_200_OK)

        return Response(Http404, status=status.HTTP_404_NOT_FOUND)


class UserProfileView(APIView):
    User = get_user_model()

    def get_object(self, email):
        try:
            queryset = self.User.objects.get(email=email)
            return queryset
        except self.User.DoesNotExist:
            raise Http404

    def get(self, request, *args, **kwargs):
        queryset = get_object_or_404(get_user_model().objects, email=request.user.email)
        serializer = UserDetailSerializer(queryset)
        return Response(serializer.data)

    def patch(self, request, *args, **kwargs):
        user = self.get_object(request.user.email)
        serializer = UserDetailSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(status.HTTP_400_BAD_REQUEST)
