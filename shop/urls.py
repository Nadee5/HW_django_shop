from django.urls import path
from django.views.decorators.cache import cache_page

from shop.apps import ShopConfig
from shop.views import home, contacts, CategoryListView, ProductListView, ProductDetailView, ProductCreateView, \
    ProductUpdateView, ProductAllListView, published_toggle

app_name = ShopConfig.name


urlpatterns = [
    path('', home, name="home"),
    path('home/', home, name="home"),
    path('contacts/', contacts, name="contacts"),
    path('catalog/', CategoryListView.as_view(), name="catalog"),
    path('products_category/<int:pk>', ProductListView.as_view(), name="products_category"),
    path('product/<int:pk>', cache_page(60)(ProductDetailView.as_view()), name="product"),
    path('all_products/', ProductAllListView.as_view(), name="all_products_list"),
    path('product/create/', ProductCreateView.as_view(), name="product_create"),
    path('product/<int:pk>/update/', ProductUpdateView.as_view(), name="product_update"),
    path('published/<int:pk>', published_toggle, name='published_toggle')
]
