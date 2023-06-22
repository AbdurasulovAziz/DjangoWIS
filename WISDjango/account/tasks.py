from django.core.mail import EmailMessage

from WISDjango import settings

from celery import shared_task


@shared_task
def send_email(email, code):
    EmailMessage(
        "UserCode",
        f"{settings.EMAIL_VERIFICATION_URL}/{email}/{code}",
        to=[email],
    ).send()
