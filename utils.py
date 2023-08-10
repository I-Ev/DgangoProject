from django.contrib.auth.tokens import default_token_generator as token_generator
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode

from config import settings

NULLABLE = {'blank': True, 'null': True}


def send_mail_verification(request, user, token):
    current_site = get_current_site(request)
    context = {
        "domain": current_site.domain,
        "user": user,
        "uid": urlsafe_base64_encode(force_bytes(user.pk)),
        "token": token,
    }

    message = render_to_string(
        'users/token_validation.html',
        context=context,
    )

    email = EmailMessage(
        'Подтверждение email',
        message,
        from_email=settings.EMAIL_HOST_USER,
        to=[user.email],
    )

    email.send()


def send_default_password(request, user, password):
    current_site = get_current_site(request)
    context = {
        "domain": current_site.domain,
        "user": user,
        "uid": urlsafe_base64_encode(force_bytes(user.pk)),
        "token": token,
    }

    message = render_to_string(
        'users/token_validation.html',
        context=context,
    )

    email = EmailMessage(
        'Подтверждение email',
        message,
        from_email=settings.EMAIL_HOST_USER,
        to=[user.email],
    )

    email.send()