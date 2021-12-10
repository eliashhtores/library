from django.views.generic import ListView
from .models import Book


class ListBooks(ListView):
    model = Book
    template_name = 'book/list.html'
    context_object_name = 'books'

    def get_queryset(self):
        keyword = self.request.GET.get('keyword', '')
        start_date = self.request.GET.get('start_date', '')
        end_date = self.request.GET.get('end_date', '')

        if start_date and end_date:
            return Book.objects.search_books_by_date(keyword, start_date, end_date)

        return Book.objects.search_books(keyword)
