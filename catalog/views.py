from django.shortcuts import render

from catalog.models import Category, Product


# Create your views here.
def home(request):
    context = {
        'object_list': Category.objects.all(),
    }
    return render(request, 'catalog/home.html', context)


def contacts(request):
    if request.method == 'POST':
        name = request.POST['name']
        phone = request.POST['phone']
        message = request.POST['message']
        print(f'name: {name}, phone: {phone}, message: {message}')
    return render(request, 'catalog/contacts.html')


def product(request, category_id):
    category = Category.objects.get(id=category_id)
    products = Product.objects.filter(category=category)
    context = {
        'object_list': products,
        'title': category.name
    }
    return render(request, 'catalog/product.html', context)
