from django.conf import settings
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.urls import path
from django.views.decorators.cache import cache_page

from blog import views
from blog.views import ArticleListView, ArticleDetailView, SearchArticleView

CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)

urlpatterns = [
    path('', cache_page(CACHE_TTL)(ArticleListView.as_view()), name='index'),
    path('article/<slug:slug>/', cache_page(CACHE_TTL)(ArticleDetailView.as_view()), name='article-detail'),
    path('search/', cache_page(CACHE_TTL)(SearchArticleView.as_view()), name='search-article'),
    path('search/<str:label>/', cache_page(CACHE_TTL)(views.SearchArticleByLabelView.as_view()),
         name='search-article-label'),
]
