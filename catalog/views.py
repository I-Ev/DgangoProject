from django.shortcuts import render

from catalog.models import Category, Product


# Create your views here.
def home(request):
    context = {
        'object_list': Product.objects.all(),
        'title': 'Интернет-магазин электроники',
        'sub_title': 'Здесь вы найдете только самое лучшее'
    }
    return render(request, 'catalog/home.html', context)


def contacts(request):
    if request.method == 'POST':
        name = request.POST['name']
        phone = request.POST['phone']
        message = request.POST['message']
        print(f'name: {name}, phone: {phone}, message: {message}')
    return render(request, 'catalog/contacts.html')


def product(request, product_id):
    product_ = Product.objects.get(id=product_id)
    context = {
        'object': product_,
        'title': product_.name
    }
    return render(request, 'catalog/product.html', context)

def categories(request):
    context = {
        'object_list': Category.objects.all(),
        'title': 'Категории товаров'
    }
    return render(request, 'catalog/categories.html', context)


def products_categ(request, category_id):
    category = Category.objects.get(id=category_id)
    products = Product.objects.filter(category=category)
    context = {
        'object_list': products,
        'title': category.name
    }
    return render(request, 'catalog/products_categ.html', context)