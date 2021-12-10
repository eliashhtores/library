from django.db import models
from django.db.models import Q


class AuthorManager(models.Manager):
    def search_author(self, author):
        return self.filter(Q(first_name__icontains=author) | Q(last_name__icontains=author))

    def search_young_author(self, author):
        return self.filter(Q(first_name__icontains=author) | Q(last_name__icontains=author)).exclude(age__gte=40)

    # def get_queryset(self):
    #     return super().get_queryset().filter(is_active=True)

    # def all_with_prefetch_books(self):
    #     return self.get_queryset().prefetch_related('books')

    # def all_with_prefetch_books_and_author(self):
    #     return self.get_queryset().prefetch_related(
    #         'books__authors',
    #         'books__authors__user'
    #     )

    # def all_with_prefetch_books_and_author_and_user(self):
    #     return self.get_queryset().prefetch_related(
    #         'books__authors__user',
    #         'books__authors__user__profile'
    #     )
