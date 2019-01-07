from django.conf import settings
from django.core.cache import cache
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.views.generic import DetailView, ListView

from blog.models import Article

CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)


class ArticleListView(ListView):
    paginate_by = 8
    template_name = 'blog/index.html'

    def get_queryset(self):
        if 'article_list' in cache:
            article_list = cache.get('article_list')
            return article_list

        article_list = Article.objects.all()
        cache.set('article_list', article_list, timeout=CACHE_TTL)
        return article_list


class ArticleDetailView(DetailView):
    model = Article

    def get_object(self):
        key = f"article_{self.kwargs['slug']}"
        if key in cache:
            article = cache.get(key)
            return article

        article = super().get_object()
        cache.set(key, article, timeout=CACHE_TTL)
        return article


class SearchArticleView(ListView):
    paginate_by = 4
    template_name = 'blog/index.html'

    def get_queryset(self):
        key = f"search_article_{self.request.GET['keyword']}"
        if key in cache:
            article_list = cache.get(key)
            return article_list

        article_list = Article.objects.filter(title__icontains=self.request.GET['keyword'])
        if article_list:
            cache.set(key, article_list, timeout=CACHE_TTL)

        return article_list


class SearchArticleByLabelView(ListView):
    paginate_by = 4
    template_name = 'blog/index.html'

    def get_queryset(self):
        key = f"search_article_label_{self.kwargs['label']}"
        if key in cache:
            article_list = cache.get(key)
            return article_list

        article_list = Article.objects.filter(label__name__exact=self.kwargs['label'])
        cache.set(key, article_list, timeout=CACHE_TTL)
        return article_list
