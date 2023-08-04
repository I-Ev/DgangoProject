from django.shortcuts import render
from django.urls import reverse_lazy, reverse

from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from pytils.translit import slugify

from blog.forms import BlogEntryForm
from blog.models import BlogEntry


class BlogEntryCreateView(CreateView):
    model = BlogEntry
    form_class = BlogEntryForm
    success_url = reverse_lazy('blog:list')

    def form_valid(self, form):
        if form.is_valid():
            new_blog_entry = form.save()
            new_blog_entry.slug = slugify(new_blog_entry.title)
            new_blog_entry.save()

            return super().form_valid(form)


class BlogEntryListView(ListView):
    model = BlogEntry

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(is_published=True)
        return queryset


class BlogEntryDetailView(DetailView):
    model = BlogEntry

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.cout_views += 1
        self.object.save()
        return self.object


class BlogEntryUpdateView(UpdateView):
    model = BlogEntry
    form_class = BlogEntryForm

    def form_valid(self, form):
        if form.is_valid():
            new_blog_entry = form.save()
            new_blog_entry.slug = slugify(new_blog_entry.title)
            new_blog_entry.save()

            return super().form_valid(form)

    def get_success_url(self):
        return reverse('blog:detail', args=[self.kwargs.get('pk')])


class BlogEntryDeleteView(DeleteView):
    model = BlogEntry
    success_url = reverse_lazy('blog:list')
