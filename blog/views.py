from django.views.generic import DetailView, ListView

from blog.models import Article


class ArticleListView(ListView):
    model = Article
    paginate_by = 4
    template_name = 'blog/index.html'


class ArticleDetailView(DetailView):
    model = Article


class SearchArticleView(ListView):
    paginate_by = 4
    template_name = 'blog/index.html'

    def get_queryset(self):
        return Article.objects.filter(title__icontains=self.request.GET['keyword'])


class SearchArticleByLabelView(ListView):
    paginate_by = 4
    template_name = 'blog/index.html'

    def get_queryset(self):
        return Article.objects.filter(label__name__exact=self.kwargs['label'])
