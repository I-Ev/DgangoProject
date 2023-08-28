from django.urls import path

from mailing.apps import MailingConfig
from mailing.tasks import setup_cronjob

from mailing.views import report, EmailCreateView, EmailUpdateView, EmailDeleteView, EmailDetailView, \
    EmailListView, MailingSettingCreateView, MailingSettingUpdateView, MailingSettingDeleteView, \
    MailingSettingDetailView, \
    MailingSettingListView, ClientListView, ClientCreateView, ClientDetailView, ClientUpdateView, ClientDeleteView

app_name = MailingConfig.name
setup_cronjob()

urlpatterns = [
    path('email/', EmailListView.as_view(), name='email_list'),
    path('email/create/', EmailCreateView.as_view(), name='email_create'),
    path('email/view/<int:pk>/', EmailDetailView.as_view(), name='email_view'),
    path('email/edit/<int:pk>/', EmailUpdateView.as_view(), name='email_update'),
    path('email/delete/<int:pk>', EmailDeleteView.as_view(), name='email_delete'),

    path('setting/', MailingSettingListView.as_view(), name='setting_list'),
    path('setting/create/', MailingSettingCreateView.as_view(), name='setting_create'),
    path('setting/view/<int:pk>/', MailingSettingDetailView.as_view(), name='setting_view'),
    path('setting/edit/<int:pk>/', MailingSettingUpdateView.as_view(), name='setting_update'),
    path('setting/delete/<int:pk>', MailingSettingDeleteView.as_view(), name='setting_delete'),

    path('client/', ClientListView.as_view(), name='client_list'),
    path('client/create/', ClientCreateView.as_view(), name='client_create'),
    path('client/view/<int:pk>/', ClientDetailView.as_view(), name='client_view'),
    path('client/edit/<int:pk>/', ClientUpdateView.as_view(), name='client_update'),
    path('client/delete/<int:pk>', ClientDeleteView.as_view(), name='client_delete'),

    path('report/', report, name='report'),

]
