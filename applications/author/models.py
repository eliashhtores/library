from django.db import models
from .managers import AuthorManager


class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    nationality = models.CharField(max_length=30)
    age = models.PositiveIntegerField(null=True, blank=True, default=0)

    objects = AuthorManager()

    def __str__(self):
        return self.first_name + ' ' + self.last_name
