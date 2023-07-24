from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from blog.apps import BlogConfig
from blog.views import BlogEntryCreateView, BlogEntryListView, BlogEntryDetailView, BlogEntryUpdateView, \
    BlogEntryDeleteView

app_name = BlogConfig.name

urlpatterns = [
    path('create/', BlogEntryCreateView.as_view(), name='create'),
    path('', BlogEntryListView.as_view(), name='list'),
    path('edit/<int:pk>', BlogEntryUpdateView.as_view(), name='edit'),
    path('view/<int:pk>', BlogEntryDetailView.as_view(), name='detail'),
    path('delete/<int:pk>/', BlogEntryDeleteView.as_view(), name='delete'),

]
