from django.db import models


class UnstopListDishManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(on_stop=False)
