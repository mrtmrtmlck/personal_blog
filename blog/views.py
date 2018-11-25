from django.shortcuts import render
from django.views.generic import DetailView, ListView

from blog.models import Article, Author


class ArticleListView(ListView):
    model = Article
    paginate_by = 5
    template_name = 'blog/index.html'


class ArticleDetailView(DetailView):
    model = Article


class AuthorDetailView(DetailView):
    model = Author


def search_article(request):
    article_list = Article.objects.filter(title__icontains=request.GET['keyword'])
    return render(request, 'blog/index.html', {'article_list': article_list})


def search_article_by_label(request, label):
    article_list = Article.objects.filter(label__name__exact=label)
    return render(request, 'blog/index.html', {'article_list': article_list})
