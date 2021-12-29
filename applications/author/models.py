from django.db import models
from .managers import AuthorManager


class Person(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    nationality = models.CharField(max_length=30)
    age = models.PositiveIntegerField(null=True, blank=True, default=0)

    class Meta:
        abstract = True

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class Author(Person):
    nickname = models.CharField(max_length=50, null=True, blank=True)

    objects = AuthorManager()
