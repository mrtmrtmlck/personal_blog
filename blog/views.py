from django.shortcuts import render
from django.views.generic import DetailView, ListView

from blog.models import Article


class ArticleListView(ListView):
    model = Article
    paginate_by = 5
    template_name = 'blog/index.html'


class ArticleDetailView(DetailView):
    model = Article
