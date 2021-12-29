from django.db import models
from django.db.models.signals import post_delete
from applications.book.models import Book
from applications.author.models import Person
from .managers import BookLoanManager
from .signals import update_book_stock


class Reader(Person):

    class Meta:
        verbose_name = 'Reader'
        verbose_name_plural = 'Readers'


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

    def save(self, *args, **kwargs):
        self.book.stock = self.book.stock - 1
        self.book.save()

        super(BookLoan, self).save(*args, **kwargs)


post_delete.connect(update_book_stock, sender=BookLoan)
