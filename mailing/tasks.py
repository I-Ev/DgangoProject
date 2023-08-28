from django.core.mail import send_mail
from django.conf import settings
from django.utils import timezone
from mailing.models import MailingSetting, SendingTry
from crontab import CronTab

def start_mailing():
    now = timezone.now()
    upcoming_mailings = MailingSetting.objects.filter(datetime__gt=now)

    for mailing in upcoming_mailings:
        # Проверяем, если время наступило, то запускаем рассылку
        if mailing.datetime <= now:
            clients = mailing.clients.all()
            subject = mailing.email.subject
            message = mailing.email.body
            from_email = settings.EMAIL_HOST_USER

            for client in clients:
                try:
                    sent = send_mail(subject, message, from_email, [client.email], fail_silently=False)
                    sending_try_status = 'успешно' if sent == 1 else 'ошибка'

                    # Создание объекта SendingTry
                    sending_try = SendingTry.objects.create(
                        status=sending_try_status,
                        client=client,
                        email=mailing.email,
                    )
                except Exception as e:
                    # Если что-то пошло не так при отправке, записываем ошибку в server_status
                    sending_try = SendingTry.objects.create(
                        status='ошибка',
                        client=client,
                        server_status=str(e),
                        email=mailing.email,
                    )

            # Обновляем статус рассылки
            mailing.status = 'Завершена'
            mailing.save()





def setup_cronjob():
    cron = CronTab(user=True)
    cron.remove_all()  # Удаляем другие задачи

    # Добавляем задачу для запуска рассылки каждый день в полночь
    job = cron.new(command='python manage.py crontab run start_mailing')
    job.setall('0 0 * * *')

    cron.write()
