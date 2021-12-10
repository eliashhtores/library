from django.contrib import admin
from .models import Book, Category


class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'category')
    search_fields = ('title', )
    ordering = ('title', 'category')
    list_filter = ('category', )


admin.site.register(Book, BookAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    ordering = ('name',)
    list_filter = ('name', )


admin.site.register(Category, CategoryAdmin)
