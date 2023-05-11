from django.db.models import Count, Sum
from django.shortcuts import render
from app.models import FoodMenu
# Create your views here.


def main(request):
    return render(request, 'app/app.html')
