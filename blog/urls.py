from django.urls import path

from blog import views
from blog.views import ArticleListView, ArticleDetailView

urlpatterns = [
    path('', ArticleListView.as_view(), name='index'),
    path('article/<slug:slug>/', ArticleDetailView.as_view(), name='article-detail'),
    path('search/', views.search_article, name='search-article'),
    path('search/<str:label>/', views.search_article_by_label, name='search-article-label'),
]
