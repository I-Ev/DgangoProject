from django.db import models

from utils import NULLABLE


# Create your models here.
class Client(models.Model):
    name = models.CharField(max_length=200, verbose_name='Имя')
    surname = models.CharField(max_length=200, verbose_name='Фамилия')
    patrony = models.CharField(max_length=200, verbose_name='Отчество')
    email = models.EmailField(max_length=200, verbose_name='Email')
    comment = models.TextField(**NULLABLE, verbose_name='Комментарий')

    def __str__(self):
        return f'{self.name} {self.surname}: {self.email}'

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'


class MailingSetting(models.Model):
    datetime = models.DateTimeField(verbose_name='Дата')
    periodicity = models.CharField(max_length=200, verbose_name='Периодичность', choices=[
        ('daily', 'раз в день'),
        ('weekly', 'раз в неделю'),
        ('monthly', 'раз в месяц')
    ])
    status = models.CharField(max_length=200, default='created', verbose_name='Статус', choices=[
        ('created', 'Создана'),
        ('in_progress', 'Запущена'),
        ('completed', 'Завершена')
    ])
    clients = models.ManyToManyField(Client, verbose_name='Клиенты')

    def __str__(self):
        return f'{self.datetime} / {self.periodicity} / {self.status}'

    class Meta:
        verbose_name = 'Настройка рассылки'
        verbose_name_plural = 'Настройки рассылки'


class Email(models.Model):
    body = models.TextField(verbose_name='Тело письма')
    subject = models.CharField(max_length=200, verbose_name='Тема письма')
    mailing_setting = models.ForeignKey(MailingSetting, on_delete=models.CASCADE,verbose_name='Настройка рассылки')

    def __str__(self):
        return self.subject

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'


class SendingTry(models.Model):
    datetime = models.DateTimeField(verbose_name='Дата и время попытки', auto_now_add=True)
    status = models.CharField(max_length=200, verbose_name='Статус попытки')
    client = models.ForeignKey(Client, on_delete=models.SET_NULL, null=True, related_name='logs')
    server_status = models.CharField(**NULLABLE, max_length=200, verbose_name='Статус сервера')
    email = models.ForeignKey(Email, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.datetime} / {self.status} / {self.server_status}'

    class Meta:
        verbose_name = 'Попытка рассылки'
        verbose_name_plural = 'Попытки рассылки'
