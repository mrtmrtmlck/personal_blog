"""personal_blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.urls import include, path, re_path
from django.views.decorators.cache import cache_page
from django.views.generic import RedirectView, TemplateView
from django.contrib.sitemaps.views import sitemap

from sitemaps import StaticViewSitemap, BlogSitemap

sitemaps = {
    'static': StaticViewSitemap,
    'blog': BlogSitemap,
}

CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('blog/', include('blog.urls')),
                  path('', RedirectView.as_view(url='/about')),
                  path('about/', cache_page(CACHE_TTL)(TemplateView.as_view(template_name='about.html')), name='about'),
                  path('google71ed5deb4b3fc51d.html',
                       TemplateView.as_view(template_name='google71ed5deb4b3fc51d.html')),
                  path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
                  re_path(r'^robots\.txt', include('robots.urls')),
                  re_path(r'^ckeditor/', include('ckeditor_uploader.urls')),
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
