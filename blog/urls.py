from django.urls import path

from blog.apps import BlogConfig
from blog.views import BlogCreateView, BlogUpdateView, BlogListView, BlogDetailView, BlogDeleteView, published_toggle

app_name = BlogConfig.name


urlpatterns = [
    path('', BlogListView.as_view(), name="blog_list"),
    path('create/', BlogCreateView.as_view(), name="blog_create"),
    path('update/<slug:slug>', BlogUpdateView.as_view(), name="blog_update"),
    path('detail/<slug:slug>', BlogDetailView.as_view(), name="blog_detail"),
    path('delete/<slug:slug>', BlogDeleteView.as_view(), name="blog_delete"),
    path('published/<int:pk>', published_toggle, name='published_toggle')
]
