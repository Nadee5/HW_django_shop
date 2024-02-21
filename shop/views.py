from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin, PermissionRequiredMixin
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from django.forms import inlineformset_factory
from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from pytils.translit import slugify

from shop.forms import ProductForm, VersionForm
from shop.models import Category, Product, Version


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


class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product
    extra_context = {
        'title': 'Информация о товаре',
    }


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('shop:home')

    def form_valid(self, form):
        if form.is_valid():
            new_product = form.save()
            new_product.slug = slugify(new_product.name)
            new_product.owner = self.request.user
            new_product.save()

            return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    #permission_required = 'shop.change_product'

    # def get_object(self, queryset=None):
    #     self.object = super().get_object(queryset)
    #     if self.object != self.request.user:
    #         raise Http404
    #     return self.object

    def get_success_url(self, *args, **kwargs):
        return reverse('shop:home', args=[self.get_object().pk])

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        VersionFormset = inlineformset_factory(Product, Version, form=VersionForm, extra=1)
        if self.request.method == 'POST':
            context_data['formset'] = VersionFormset(self.request.POST, instance=self.object)
        else:
            context_data['formset'] = VersionFormset(instance=self.object)
        return context_data

    def form_valid(self, form):
        formset = self.get_context_data()['formset']
        self.object = form.save()
        if formset.is_valid():
            formset.instance = self.object
            formset.save()
        return super().form_valid(form)

    # def test_func(self):
    #     if self.request.user == self.product.owner:
    #         content_type = ContentType.objects.get_for_model(Product)
    #         permissions = Permission.objects.get(
    #             codename="change_product",
    #             content_type=content_type,
    #         )
    #         self.user.user_permissions.add(permissions)


class ProductAllListView(ListView):
    model = Product
    form_class = ProductForm
    template_name = 'shop/all_products_list.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        if not self.request.user.is_staff:
            queryset = queryset.filter(is_published=True)
        return queryset

@login_required
@permission_required('shop.set_published')
def published_toggle(request, pk):
    product_item = get_object_or_404(Product, pk=pk)
    if product_item.is_published:
        product_item.is_published = False
    else:
        product_item.is_published = True
    product_item.save()
    return redirect(reverse('shop:home'))






