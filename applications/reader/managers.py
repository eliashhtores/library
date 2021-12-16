from django.db import models
from django.db.models import Avg, Sum, Count


class BookLoanManager(models.Manager):
    def get_average_age(self):
        return self.filter(book_id=5).aggregate(Avg('reader__age'), Sum('reader__age'))

    def num_book_loans(self):
        results = self.values('book').annotate(loans=Count('book'))
        for result in results:
            print(result, result['loans'])
        return results
