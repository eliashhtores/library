from django.urls import path
from . import views

urlpatterns = [
    path('books/list', views.ListBooks.as_view(), name='list'),
    path('books/list-category',
         views.CategoriesByAuthor.as_view(), name='author_category'),
    path('books/detail/<pk>', views.BookDetail.as_view(), name='detail'),
]
