from django.shortcuts import render
from django.urls import reverse_lazy
from pytils.translit import slugify
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView

from mailing.forms import EmailForm, MailingSettingForm
from mailing.models import Email, MailingSetting, Client


# CRUD для модели Email
class EmailCreateView(CreateView):
    model = Email
    form_class = EmailForm


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
