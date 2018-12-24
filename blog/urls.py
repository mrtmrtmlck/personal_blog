from django.urls import path

from blog import views
from blog.views import ArticleListView, ArticleDetailView, SearchArticleView

urlpatterns = [
    path('', ArticleListView.as_view(), name='index'),
    path('article/<slug:slug>/', ArticleDetailView.as_view(), name='article-detail'),
    path('search/', SearchArticleView.as_view(), name='search-article'),
    path('search/<str:label>/', views.SearchArticleByLabelView.as_view(), name='search-article-label'),
]
