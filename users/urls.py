from django.contrib.auth.views import LogoutView
from django.urls import path

from users.apps import UsersConfig
from users.views import RegisterView, ProfileView, LoginView_Mixin, get_info_page, \
    VerifyEmailView, get_success_email_page, get_reset_done, reset_password

app_name = UsersConfig.name

urlpatterns = [
    path('login/', LoginView_Mixin.as_view(template_name='users/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('profile/', ProfileView.as_view(), name='profile'),

    path('verify_email/<uidb64>/<token>/', VerifyEmailView.as_view(), name='verify'),
    path('info_page/', get_info_page, name='info_page'),
    path('success_email_verify/', get_success_email_page, name='succes_page'),

    path("password_reset/", reset_password, name="recovery"),
    path("password_reset_done/", get_reset_done, name="recovery_done"),

]
