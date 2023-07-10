from django.urls import path

from catalog.views import contacts, home

urlpatterns = [
    path('', contacts, name='contacts'),
    path('', home, name='home')
]