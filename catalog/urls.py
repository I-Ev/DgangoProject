from django.urls import path

from catalog.views import contacts, home

urlpatterns = [
    path('', contacts),
    path('', home)
]