from django.db import models
from applications.book.models import Book
from .managers import BookLoanManager


class Reader(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    nationality = models.CharField(max_length=30)
    age = models.PositiveIntegerField(null=True, blank=True, default=0)

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class BookLoan(models.Model):
    reader = models.ForeignKey(Reader, on_delete=models.CASCADE)
    book = models.ForeignKey(
        Book, on_delete=models.CASCADE, related_name='loan_book')
    loan_date = models.DateField(auto_now_add=True)
    return_date = models.DateField(null=True, blank=True)
    returned = models.BooleanField(default=False)

    objects = BookLoanManager()

    def __str__(self):
        return self.book.title + ' - ' + self.reader.first_name + ' ' + self.reader.last_name
