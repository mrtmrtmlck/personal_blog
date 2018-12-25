from django.contrib.sitemaps import Sitemap
from django.urls import reverse

from blog.models import Article


class BlogSitemap(Sitemap):
    changefreq = "weekly"
    priority = 1.0
    protocol = 'https'

    def items(self):
        return Article.objects.all()

    def lastmod(self, obj):
        return obj.modified_at


class StaticViewSitemap(Sitemap):
    priority = 0.5
    changefreq = 'yearly'
    protocol = 'https'

    def items(self):
        return ['about', ]

    def location(self, item):
        return reverse(item)
