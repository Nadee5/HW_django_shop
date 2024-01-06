from django.urls import path

from shop.apps import ShopConfig
from shop.views import home, contacts, CategoryListView, ProductListView, ProductDetailView

app_name = ShopConfig.name


urlpatterns = [
    path('', home, name="home"),
    path('home/', home, name="home"),
    path('contacts/', contacts, name="contacts"),
    path('catalog/', CategoryListView.as_view(), name="catalog"),
    path('products_category/<int:pk>', ProductListView.as_view(), name="products_category"),
    path('product/<int:pk>', ProductDetailView.as_view(), name="product"),
]
