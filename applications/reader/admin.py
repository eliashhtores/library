from django.contrib import admin
from .models import Reader


class ReaderAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name')
    search_fields = ('first_name', 'last_name')
    ordering = ('first_name', 'last_name')


admin.site.register(Reader, ReaderAdmin)
