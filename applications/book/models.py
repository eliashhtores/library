from django.db import models
from django.db.models.signals import post_save
from applications.author.models import Author
from .managers import BookManager, CategoryManager
from .signals import optimize_image


class Category(models.Model):
    name = models.CharField(max_length=100)

    objects = CategoryManager()

    class Meta:
        verbose_name = ('Categorie')

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=100)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name='book_category')
    authors = models.ManyToManyField(Author)
    release_date = models.DateField()
    cover = models.ImageField(upload_to='covers/', null=True, blank=True)
    visits = models.PositiveIntegerField(default=0)
    stock = models.PositiveIntegerField(default=1)

    objects = BookManager()

    def __str__(self):
        return self.title


post_save.connect(optimize_image, sender=Book)
