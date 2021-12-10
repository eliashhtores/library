from datetime import datetime
from django.db import models
from django.db.models import Q


class BookManager(models.Manager):
    def search_books(self, title):
        return self.filter(title__icontains=title).order_by('title')

    def search_books_by_date(self, title, start_date, end_date):
        return self.filter(title__icontains=title, release_date__range=(datetime.strptime(start_date, '%Y-%m-%d').date(), datetime.strptime(end_date, '%Y-%m-%d').date())).order_by('release_date')
