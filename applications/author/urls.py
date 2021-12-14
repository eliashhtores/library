from django.urls import path
from . import views

urlpatterns = [
    path('authors/list', views.ListAuthors.as_view(), name='list'),
]
