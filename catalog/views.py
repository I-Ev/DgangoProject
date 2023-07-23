from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView

from catalog.models import Category, Product


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
        category = Category.objects.get(id=self.kwargs['category_id'])
        context['title'] = category.name
        return context
