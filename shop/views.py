from django.shortcuts import render

from shop.models import Category, Product


def home(request):
    return render(request, 'shop/home.html')


def catalog(request):
    context = {
        'object_list': Category.objects.all(),
        'title': 'Категории товаров',
    }
    return render(request, 'shop/catalog.html', context)


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'{name} ({phone}): {message}')
    return render(request, 'shop/contacts.html')


def products_category(request, pk):
    category_item = Category.objects.get(pk=pk)
    context = {
        'object_list': Product.objects.filter(category_id=pk),
        'title': f'Все товары категории: {category_item.name}',
    }
    return render(request, 'shop/products_category.html', context)


def product(request, pk):
    context = {
        'object_list': Product.objects.filter(id=pk),
    }
    return render(request, 'shop/product.html', context)




