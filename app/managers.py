from django.db import models


class NonAlcoholicDrinkManager(models.Manager):

    def get_queryset(self):
        return super().get_queryset().exclude(category='Алкогольные напитки')
