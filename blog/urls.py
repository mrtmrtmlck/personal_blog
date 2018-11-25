from django.urls import path

from blog.views import ArticleListView, ArticleDetailView

urlpatterns = [
    path('', ArticleListView.as_view(), name='index'),
    path('<int:pk>/<slug:slug>/', ArticleDetailView.as_view(), name='article-detail'),
]
