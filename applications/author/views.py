from django.views.generic import ListView
from .models import Author


class ListAuthors(ListView):
    template_name = 'author/list.html'
    context_object_name = 'authors'

    def get_queryset(self):
        keyword = self.request.GET.get('keyword', '')
        return Author.objects.search_young_author(keyword)
