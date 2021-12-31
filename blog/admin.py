from typing import Callable
from django.contrib import admin
from .models import Category, Post

class PostAdmin(admin.ModelAdmin):
    date_hierarchy = 'published_date'
    empty_value_display = '-empty-'
    list_display = ('title', 'author', 'counted_views', 'status', 'published_date')
    list_filter = ('status', 'author')
    ordering = ('-created_date',)
    search_fields = ('title', 'content')

admin.site.register(Category)    
admin.site.register(Post, PostAdmin)    