from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView

from blog.models import BlogEntry


class BlogEntryCreateView(CreateView):
    model = BlogEntry
    fields = ['title', 'body', 'preview']
    success_url = reverse_lazy('blog:list')

class BlogEntryListView(ListView):
    model = BlogEntry

class BlogEntryDetailView(DetailView):
    model = BlogEntry