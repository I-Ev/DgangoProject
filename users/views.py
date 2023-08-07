import random

from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.hashers import make_password
from django.contrib.auth.views import LoginView
from django.core.mail import send_mail
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse_lazy, reverse
from django.views import View
from django.views.generic import CreateView, UpdateView, DetailView
import secrets

from config import settings
from config.settings import EMAIL_HOST_USER
from users.forms import UserRegisterForm, UserProfileForm, AuthenticationForm_Mixin
from users.models import User


class RegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:info_page')

    # def form_valid(self, form):
    #     user = form.save(commit=False)
    #     user.generate_verification_token()  # Генерация токена
    #     user.save()
    #
    #     token = user.verification_token
    #     verification_url = self.request.build_absolute_uri(reverse('users:verify')) + f'?token={token}'
    #
    #     send_mail(
    #         subject='Подтвердите email',
    #         message=f'Для подтверждения email перейдите на {verification_url}',
    #         from_email=settings.EMAIL_HOST_USER,
    #         recipient_list=[user.email],
    #     )
    #     return super().form_valid(form)


class ProfileView(UpdateView):
    model = User
    form_class = UserProfileForm
    success_url = reverse_lazy('users:profile')

    def get_object(self, queryset=None):
        return self.request.user


@login_required
def get_new_password(request):
    new_password = ''.join([str(random.randint(0, 9)) for _ in range(8)])
    send_mail(
        'Сброс пароля',
        'Ваш новый пароль: {0}'.format(new_password),
        EMAIL_HOST_USER,
        request.user.email
    )
    logout(request)
    request.user.set_password(new_password)
    request.user.save()
    return redirect(reverse_lazy('catalog:home'))

    # if request.method == 'POST':
    #     email = request.POST.get('email')
    #     if not email:
    #         return HttpResponseBadRequest('Не указан email')
    #
    #     user = User.objects.get(email=email)
    #     new_password = user.objects.make_random_password()
    #     user.set_password(new_password)
    #     user.save()
    #
    #     send_mail(
    #         'Сброс пароля',
    #         'Ваш новый пароль: {0}'.format(new_password),
    #         EMAIL_HOST_USER,
    #         [email]
    #     )
    #
    #     return HttpResponseRedirect('login')


class LoginView_Mixin(LoginView):
    form_class = AuthenticationForm_Mixin


def recovery_page(request):
    return render(request, 'users/recovery.html')


class VerifyEmailView(View):
    model = User
    template_name = 'users/token_validation.html'

    def get(self, request, *args, **kwargs):
        token = kwargs.get('token')
        try:
            user = User.objects.get(verification_token=token)
            user.is_email_verified = True
            user.verification_token = None
            user.save()
            return HttpResponse('Email подтвержден')
        except User.DoesNotExist:
            return HttpResponse('Неверная ссылка')


def get_info_page(request):
    return render(request, 'users/info_page.html')
