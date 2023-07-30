from django.urls import path

from mailing.apps import MailingConfig

from mailing.views import report, EmailCreateView, EmailUpdateView, EmailDeleteView, EmailDetailView, \
    EmailListView, MailingSettingCreateView, MailingSettingUpdateView, MailingSettingDeleteView, MailingSettingDetailView, \
    MailingSettingListView

app_name = MailingConfig.name

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
    path('report/', report, name='report'),

]
