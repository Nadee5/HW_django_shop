from django.contrib import admin

from blog.models import Blog


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    # list_display = ('pk', 'title', 'date_of_create', 'is_published', 'views_count',)
    # list_filter = ('is_published',)
    search_fields = ('title',)
    sortable_by = ('date_of_create',)

