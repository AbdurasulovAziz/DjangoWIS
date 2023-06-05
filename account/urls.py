from django.urls import path, include
from account import views
from django.contrib.auth import views as auth_views

urlpatterns = [

    # path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    # path(
    #     "password_change/",
    #     auth_views.PasswordChangeView.as_view(
    #         template_name="account/password_change.html"
    #     ),
    #     name="password_change",
    # ),
    # path(
    #     "password_change/done/",
    #     auth_views.PasswordChangeDoneView.as_view(
    #         template_name="account/password_change_done.html"
    #     ),
    #     name="password_change_done",
    # ),
    # path(
    #     "password_reset/",
    #     auth_views.PasswordResetView.as_view(
    #         template_name="account/password_reset_form.html"
    #     ),
    #     name="password_reset",
    # ),
    # # path("password_reset_form")
    # path(
    #     "password_reset/done/",
    #     auth_views.PasswordResetDoneView.as_view(
    #         template_name="account/password_reset_done.html"
    #     ),
    #     name="password_reset_done",
    # ),
    # path(
    #     "reset/<uidb64>/<token>/",
    #     auth_views.PasswordResetConfirmView.as_view(
    #         template_name="account/password_reset_confirm.html"
    #     ),
    #     name="password_reset_confirm",
    # ),
    # path(
    #     "reset/done/",
    #     auth_views.PasswordResetCompleteView.as_view(
    #         template_name="account/password_reset_complete.html"
    #     ),
    #     name="password_reset_complete",
    # ),
    path("registration/", views.UserRegistrationView.as_view(), name="registration"),
    path(
        "verify/<str:email>/<str:activation_key>",
        views.UserRegistrationVerifyView.as_view(),
        name="verify",
    ),
    path("profile/", views.UserProfileView.as_view(), name="profile"),
]
