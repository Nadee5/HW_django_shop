from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView

from shop.forms import ProductForm
from shop.models import Category, Product


def home(request):
    return render(request, 'shop/home.html')


class CategoryListView(ListView):
    model = Category
    extra_context = {
        'title': 'Категории товаров',
    }


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'{name} ({phone}): {message}')
    return render(request, 'shop/contacts.html')


class ProductListView(ListView):
    model = Product

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(category_id=self.kwargs.get('pk'))
        return queryset


class ProductDetailView(DetailView):
    model = Product
    extra_context = {
        'title': '',
    }


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    success_url = 'shop:home' #market


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    success_url = 'shop:home' #market


class ProductAllListView(ListView):
    model = Product
    form_class = ProductForm
    template_name = 'shop/all_products_list/html'








