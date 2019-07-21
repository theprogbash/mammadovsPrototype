from django.contrib import admin
from .models import Category, Article


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('category', 'title', 'description', 'content', 'post_date', 'image', 'slug')


admin.site.register(Category)
admin.site.register(Article, ArticleAdmin)

