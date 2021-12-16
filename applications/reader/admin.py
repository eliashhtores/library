from django.contrib import admin
from .models import Reader, BookLoan


class ReaderAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name')
    search_fields = ('first_name', 'last_name')
    ordering = ('first_name', 'last_name')


admin.site.register(Reader, ReaderAdmin)


class BookLoanAdmin(admin.ModelAdmin):
    list_display = ('book', 'reader', 'return_date', 'returned')
    ordering = ('book', 'reader')


admin.site.register(BookLoan, BookLoanAdmin)
