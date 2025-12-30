from django.contrib import admin
from .models import Category, Blog
# Register your models here.

class BlogAdmin(admin.ModelAdmin):
    
    list_display = ('title', 'category', 'author', 'is_featured', 'created_at', 'updated_at', 'status')
    search_fields = ('id', 'title', 'category__category_name', 'status')
    list_editable = ('is_featured', )
    readonly_fields = ('slug',)
admin.site.register(Category)
admin.site.register(Blog, BlogAdmin)
