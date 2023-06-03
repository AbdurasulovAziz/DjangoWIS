from django import forms


class DishAddToCartForm(forms.Form):
    count = forms.IntegerField()
