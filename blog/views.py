from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView

from blog.models import BlogEntry


class BlogEntryCreateView(CreateView):
    model = BlogEntry
    fields = ['title', 'body', 'preview']
    success_url = reverse_lazy('catalog:home')

class BlogEntryListView(ListView):
    model = BlogEntry

