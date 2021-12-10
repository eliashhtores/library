from django.db import models
from applications.author.models import Author
from .managers import BookManager


class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = ('Categorie')

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    authors = models.ManyToManyField(Author)
    release_date = models.DateField()
    cover = models.ImageField(upload_to='covers/', null=True, blank=True)
    visits = models.PositiveIntegerField(default=0)

    objects = BookManager()

    def __str__(self):
        return self.title
