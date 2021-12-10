from django.urls import path
from . import views

urlpatterns = [
    path('list-authors/', views.ListAuthors.as_view(), name='list_authors'),
]
