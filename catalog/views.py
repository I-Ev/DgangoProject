from django.shortcuts import render

from catalog.models import Category


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

def product(request):
    # context = {
    #     'object_list': Category.objects.all(),
    # }
    return render(request, 'catalog/product.html')