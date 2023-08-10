from django.contrib.auth.views import LogoutView
from django.urls import path

from users.apps import UsersConfig
from users.views import RegisterView, ProfileView, get_new_password, LoginView_Mixin, recovery_page, get_info_page, VerifyEmailView

app_name = UsersConfig.name

urlpatterns = [
    path('login/', LoginView_Mixin.as_view(template_name='users/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('profile/', ProfileView.as_view(), name='profile'),

    path('verify_email/<uidb64>/<token>/', VerifyEmailView.as_view(), name='verify'),
    path('info_page/', get_info_page, name='info_page'),

    # path('recovery/', recovery_page, name='recovery_page'),
    path('recovery/', get_new_password, name='recovery'),
]


