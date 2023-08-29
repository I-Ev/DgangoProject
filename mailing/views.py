from django.core.mail import send_mail
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils import timezone
from pytils.translit import slugify
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView

from config import settings
from mailing.forms import EmailForm, MailingSettingForm
from mailing.models import Email, MailingSetting, Client, SendingTry


# CRUD для модели Email
class EmailCreateView(CreateView):
    model = Email
    form_class = EmailForm

    def form_valid(self, form):
        instance = form.save(commit=False)
        now = timezone.now()

        if instance.datetime_start <= now:
            # Запускаем рассылку сразу
            settings = instance.mailing_setting
            settings.status = 'Запущена'
            settings.save()

            clients = settings.clients.all()
            subject = instance.subject
            message = instance.body
            from_email = settings.EMAIL_HOST_USER
            for client in clients:
                try:
                    sent = send_mail(subject, message, from_email, [client.email], fail_silently=False)
                    sending_try_status = 'успешно' if sent == 1 else 'ошибка'

                    # Создание объекта SendingTry
                    sending_try = SendingTry.objects.create(
                        status=sending_try_status,
                        client=client,
                        email=instance
                    )
                except Exception as e:
                    # Если что-то пошло не так при отправке, записываем ошибку в server_status

                    sending_try = SendingTry.objects.create(
                        status='ошибка',
                        client=client,
                        server_status=str(e),
                        email=instance
                    )

                # Обновление статуса рассылки
                settings.status = 'Завершена'
                settings.save()

        elif instance.datetime_start > now:
            pass
        # Рассылку нужно запустить в будущем
        # Здесь можно реализовать запуск рассылки по наступлению времени datetime_start
        # Например, используя Celery для отложенных задач

        return reverse_lazy('mailing:email_list')  # Перенаправление на список рассылок


class EmailListView(ListView):
    model = Email


class EmailDetailView(DetailView):
    model = Email


class EmailUpdateView(UpdateView):
    model = Email
    form_class = EmailForm


class EmailDeleteView(DeleteView):
    model = Email
    success_url = reverse_lazy('mailing:email_list')


###########################################################

# CRUD для модели MailingSetting
class MailingSettingCreateView(CreateView):
    model = MailingSetting
    form_class = MailingSettingForm
    success_url = reverse_lazy('mailing:setting_list')


class MailingSettingListView(ListView):
    model = MailingSetting


class MailingSettingDetailView(DetailView):
    model = MailingSetting


class MailingSettingUpdateView(UpdateView):
    model = MailingSetting
    form_class = MailingSettingForm
    success_url = reverse_lazy('mailing:setting_list')


class MailingSettingDeleteView(DeleteView):
    model = MailingSetting
    success_url = reverse_lazy('mailing:setting_list')


#########################################################################


# CRUD для модели Client
class ClientCreateView(CreateView):
    model = Client
    fields = ['name', 'surname', 'patrony', 'email', 'comment']
    success_url = reverse_lazy('mailing:client_list')


class ClientListView(ListView):
    model = Client


class ClientDetailView(DetailView):
    model = Client


class ClientUpdateView(UpdateView):
    model = Client
    fields = ['name', 'surname', 'patrony', 'email', 'comment']
    success_url = reverse_lazy('mailing:client_list')


class ClientDeleteView(DeleteView):
    model = Client
    success_url = reverse_lazy('mailing:client_list')


#########################################################################
# Отчет о проведенных рассылках
class report(ListView):
    model = SendingTry