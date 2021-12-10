from django.urls import path
from . import views

urlpatterns = [
    path('list-books/', views.ListBooks.as_view(), name='list_books'),
]
