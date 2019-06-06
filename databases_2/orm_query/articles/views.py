from django.views.generic import ListView

from .models import Article


class ArticleListView(ListView):
    template_name = 'articles/news.html'
    model = Article
    ordering = '-published_at'

    def get_queryset(self):
        queryset = Article.objects.prefetch_related('author', 'genre')
        return queryset

