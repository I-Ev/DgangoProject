from django.core.cache import cache
from django.forms import inlineformset_factory
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, TemplateView, CreateView, UpdateView

from catalog.forms import ProductForm, VersionForm
from catalog.models import Category, Product, Version
from catalog.services import get_cached_categories_list
from config import settings


class HomeView(ListView):
    model = Product
    template_name = 'catalog/home.html'
    context_object_name = 'object_list'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Интернет-магазин электроники'
        context['sub_title'] = 'Здесь вы найдете только самое лучшее'
        return context


def contacts(request):
    if request.method == 'POST':
        name = request.POST['name']
        phone = request.POST['phone']
        message = request.POST['message']
        print(f'name: {name}, phone: {phone}, message: {message}')
    return render(request, 'catalog/contacts.html')


class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog/product.html'

    # если кэшировать не на уровне контроллера:
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #
    #     product = self.object
    #
    #     name_key = f'product_{product.id}_name'
    #     desc_key = f'product_{product.id}_desc'
    #
    #     context['product_name'] = cache.get(name_key)
    #     if context['product_name'] is None:
    #         context['product_name'] = product.name
    #         cache.set(name_key, context['product_name'], 60 * 15)
    #
    #     context['product_desc'] = cache.get(desc_key)
    #     if context['product_desc'] is None:
    #         context['product_desc'] = product.description
    #         cache.set(desc_key, context['product_desc'], 60 * 15)
    #
    #     return context


class CategoriesListView(ListView):
    model = Category
    template_name = 'catalog/categories.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Категории товаров'
        return context


class ProductsCategListView(ListView):
    model = Product
    template_name = 'catalog/products_categ.html'

    def get_queryset(self):
        return Product.objects.filter(category=self.kwargs['category_id'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Получение списка категорий через сервисную функцию с кэшированием
        category_list = get_cached_categories_list()
        context['category_list'] = category_list

        # Добавление данных к контексту
        category = Category.objects.get(id=self.kwargs['category_id'])
        context['title'] = category.name
        return context


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:home')

    def form_valid(self, form):
        user = self.request.user
        form.instance.user_created = user
        form.save()
        return super().form_valid(form)


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        VersionFormset = inlineformset_factory(
            Product, Version, form=VersionForm, extra=1
        )
        if self.request.method == 'POST':
            context['formset'] = VersionFormset(self.request.POST, instance=self.object)
        else:
            context['formset'] = VersionFormset(instance=self.object)
        return context

    def form_valid(self, form):
        formset = self.get_context_data()['formset']
        self.object = form.save()

        if formset.is_valid():
            formset.instance = self.object
            formset.save()

        return super().form_valid(form)
