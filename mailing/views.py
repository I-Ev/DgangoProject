from django.shortcuts import render
from django.urls import reverse_lazy
from pytils.translit import slugify
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView

from mailing.models import Email, MailingSetting


# CRUD для модели Email
class EmailCreateView(CreateView):
    model = Email
    fields = ['subject', 'body', 'mailing_setting']


class EmailListView(ListView):
    model = Email


class EmailDetailView(DetailView):
    model = Email


class EmailUpdateView(UpdateView):
    model = Email
    fields = ['subject', 'body', 'mailing_setting']


class EmailDeleteView(DeleteView):
    model = Email
    success_url = reverse_lazy('mailing:email_list')
###########################################################

# CRUD для модели MailingSetting
class MailingSettingCreateView(CreateView):
    model = MailingSetting
    fields = ['date', 'time', 'periodicity']
    success_url = reverse_lazy('mailing:email_list')


class MailingSettingListView(ListView):
    model = MailingSetting


class MailingSettingDetailView(DetailView):
    model = MailingSetting


class MailingSettingUpdateView(UpdateView):
    model = MailingSetting
    fields = ['date', 'time', 'periodicity']
    success_url = reverse_lazy('mailing:setting_list')


class MailingSettingDeleteView(DeleteView):
    model = MailingSetting
    success_url = reverse_lazy('mailing:setting_list')
#########################################################################

def report(request):
    emails = Email.objects.all()
    email_settings = MailingSetting.objects.filter(status__neq='created')

    context = {
        'email_list': Email.objects.filter(status__neq='created')
    }

    return render(request, 'mailing/report.html')


def report(request):
    return render(request, 'mailing/report.html', {
        'email_list': Email.objects.filter(status__neq='created')
    })
