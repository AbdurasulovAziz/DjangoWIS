from django.core.exceptions import ValidationError
import datetime


def birth_date_validation(value):
    if value > datetime.date.today():
        raise ValidationError(
            'Bad birth day'
        )
