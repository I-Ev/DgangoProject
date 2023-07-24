from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView

from blog.models import BlogEntry


class BlogEntryCreateView(CreateView):
    model = BlogEntry
    fields = ['title', 'body', 'preview']
    success_url = reverse_lazy('blog:list')


class BlogEntryListView(ListView):
    model = BlogEntry


class BlogEntryDetailView(DetailView):
    model = BlogEntry


class BlogEntryUpdateView(UpdateView):
    model = BlogEntry
    fields = ['title', 'body', 'preview']
    success_url = reverse_lazy('blog:list')


class BlogEntryDeleteView(DeleteView):
    model = BlogEntry
    success_url = reverse_lazy('blog:list')

