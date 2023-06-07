from django.urls import path
from app import views


urlpatterns = [
    path("food/", views.FoodPage.as_view(), name="food-page"),
    path("food/<int:pk>/", views.FoodDetailPage.as_view(), name="food-detail"),
    path("dessert/", views.DessertPage.as_view(), name="dessert-page"),
    path("dessert/<int:pk>/", views.DessertDetailPage.as_view(), name="dessert-detail"),
    path("sauce/", views.SaucePage.as_view(), name="sauce-page"),
    path("sauce/<int:pk>/", views.SauceDetailPage.as_view(), name="sauce-detail"),
    path("drink/", views.DrinkPage.as_view(), name="drink-page"),
    path("drink/<int:pk>/", views.DrinkDetailPage.as_view(), name="drink-detail"),
    path("boxmix/", views.BoxMixPage.as_view(), name="boxmix-page"),
    path("boxmix/<int:pk>/", views.BoxMixDetailPage.as_view(), name="boxmix-detail"),
    path("cart/", views.CartPageView.as_view(), name="cart-page"),
    path("cart/add/<int:dish_id>/", views.CartAddView.as_view(), name="cart-add"),
    path("cart/item/<int:dish_id>/", views.CartItemView.as_view()),
]
