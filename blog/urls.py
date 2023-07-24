from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from blog.apps import BlogConfig
from blog.views import BlogEntryCreateView, BlogEntryListView

app_name = BlogConfig.name

urlpatterns = [
    path('create/', BlogEntryCreateView.as_view(), name='create'),
    path('', BlogEntryListView.as_view(), name='list'),
    # path('edit/<int:pk>', ..., name='edit'),
    # path('view/<int:pk>', ..., name='view'),
    # path('delete/<int:pk>/', ..., name='delete'),

]
