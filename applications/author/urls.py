from django.urls import path
from . import views

app_name = 'author_app'

urlpatterns = [
    path('authors/list', views.ListAuthors.as_view(), name='list'),
]
