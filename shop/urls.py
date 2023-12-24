from django.urls import path

from shop.apps import ShopConfig
from shop.views import home, contacts, catalog, products_category, product

app_name = ShopConfig.name

urlpatterns = [
    path('', home, name="home"),
    path('home/', home, name="home"),
    path('contacts/', contacts, name="contacts"),
    path('catalog/', catalog, name="catalog"),
    path('<int:pk>/products_category/', products_category, name="products_category"),
    path('<int:pk>/product/', product, name="product"),
]
