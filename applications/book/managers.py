from datetime import datetime
from django.db import models
from applications.author.models import Author
from django.db.models import Q


class BookManager(models.Manager):
    def search_books(self, title):
        return self.filter(title__icontains=title).order_by('title')

    def search_books_by_date(self, title, start_date, end_date):
        return self.filter(title__icontains=title, release_date__range=(datetime.strptime(start_date, '%Y-%m-%d').date(), datetime.strptime(end_date, '%Y-%m-%d').date())).order_by('release_date')

    def add_author_book(self, author_id, book_id):
        book = self.get(pk=book_id)
        book.authors.add(author_id)
        return book


class CategoryManager(models.Manager):
    def search_category(self, name):
        return self.filter(name__icontains=name).order_by('name')

    def categories_by_author(self, author):
        return self.filter(book_category__authors__id=author).distinct().order_by('name')
