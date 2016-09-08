"""minicms URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url, include
from django.contrib import admin
import sys

from django.contrib.sitemaps import GenericSitemap
from django.contrib.sitemaps.views import sitemap
from django.views.decorators.cache import cache_page
from django.contrib.sitemaps import views as sitemaps_views

sys.path.append(settings.BASE_DIR)
from DjangoUeditor import urls as DjangoUeditor_urls
from news import views
from news.models import Article,Column

sitemaps = {
    'blog': GenericSitemap({'queryset': Article.objects.all(), 'date_field': 'pub_date'}, priority=0.6),
    'news':GenericSitemap({'queryset': Article.objects.all(),'update_time':'pub_date'},priority = 0.6),
    # 如果还要加其它的可以模仿上面的
}


urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r'^user/$',views.userinfo,name='userinfo'),
    url(r'^admin/', admin.site.urls),
    url(r'^ueditor/', include(DjangoUeditor_urls)),
    url(r'^column/(?P<column_slug>[^/]+)/$',views.column_detail,name='column'),
    url(r'^news/(?P<pk>\d+)/(?P<article_slug>[^/]+)/$',views.article_detail,name='article'),
    # 但是这样生成的 sitemap，如果网站内容太多就很慢，很耗费资源，可以采用分页的功能：
    #url(r'^sitemap\.xml$', sitemap, {'sitemaps': sitemaps},
        #name='django.contrib.sitemaps.views.sitemap'),
]
"""
   url(r'^sitemap\.xml$',
       cache_page(86400)(sitemaps_views.index),
       {'sitemaps': sitemaps, 'sitemap_url_name': 'sitemaps'}),
   url(r'^sitemap-(?P<section>.+)\.xml$',
       cache_page(86400)(sitemaps_views.sitemap),
       {'sitemaps': sitemaps}, name='sitemaps'),
   """



if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)