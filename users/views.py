import random

from django.contrib.auth import logout, get_user_model, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.hashers import make_password
from django.contrib.auth.views import LoginView
from django.core.exceptions import ValidationError
from django.core.mail import send_mail
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse_lazy, reverse
from django.utils.http import urlsafe_base64_decode
from django.views import View
from django.views.generic import CreateView, UpdateView, DetailView
from django.contrib.auth.tokens import default_token_generator as token_generator
import secrets

from config import settings
from config.settings import EMAIL_HOST_USER
from users.forms import UserRegisterForm, UserProfileForm, AuthenticationForm_Mixin
from users.models import User
from utils import send_mail_verification

User = get_user_model()

class RegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = 'users/register.html'

    success_url = reverse_lazy('users:info_page')

    def form_valid(self, form):
        user = form.save(commit=False)
        send_mail_verification(self.request, user)
        return super().form_valid(form)

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


class LoginView_Mixin(LoginView):
    form_class = AuthenticationForm_Mixin


def recovery_page(request):
    return render(request, 'users/recovery.html')


class VerifyEmailView(View):

    def get(self, request, uidb64, token):
        user = self.get_user(uidb64)
        if user is not None and token_generator.check_token(user, token):
            user.is_email_verified = True
            user.save()
            login(request, user)
            return redirect('home/')

        return HttpResponse('Неверная ссылка, скорее всего она уже устарела или пользователь не найден')


    @staticmethod
    def get_user(uidb64):
        try:
            # urlsafe_base64_decode() decodes to bytestring
            uid = urlsafe_base64_decode(uidb64).decode()
            user = User.objects.get(pk=uid)
        except (
            TypeError,
            ValueError,
            OverflowError,
            User.DoesNotExist,
            ValidationError,
        ):
            user = None
        return user



def get_info_page(request):
    return render(request, 'users/info_page.html')
