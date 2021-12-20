from datetime import datetime
from django.db import models
from django.db.models import Count
from django.contrib.postgres.search import TrigramSimilarity
from django.db.models.functions import Lower


class BookManager(models.Manager):
    def search_books(self, title):
        return self.filter(title__trigram_similar=title).order_by('title')

    def search_books_by_date(self, title, start_date, end_date):
        return self.filter(title__trigram_similar=title, release_date__range=(datetime.strptime(start_date, '%Y-%m-%d').date(), datetime.strptime(end_date, '%Y-%m-%d').date())).order_by('release_date')

    def add_author_book(self, author_id, book_id):
        book = self.get(pk=book_id)
        book.authors.add(author_id)
        return book

    def book_loans_count(self):
        return self.aggregate(loans=Count('loan_book'))

    def book_loans(self):
        results = self.annotate(loans=Count('loan_book'))
        for result in results:
            print(result, result.loans)
        # return results


class CategoryManager(models.Manager):
    def search_category(self, name):
        return self.filter(name__icontains=name).order_by('name')

    def categories_by_author(self, author):
        return self.filter(book_category__authors__id=author).distinct().order_by('name')

    def list_category_book(self):
        results = self.annotate(book_count=Count('book_category'))
        # for result in results:
        #     print(result, result.book_count)
        return results
