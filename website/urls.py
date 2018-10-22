
from django.conf.urls import url,include,re_path
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from blog.feed import LatestEntriesFeed
from blog import views as blog_views
from website.settings import STATIC_ROOT,MEDIA_ROOT
from django.views.static import serve

from django.contrib.sitemaps import GenericSitemap
from django.contrib.sitemaps.views import sitemap
from blog.models import Entry

info_dict = {
    'queryset': Entry.objects.all(),
    'date_field': 'modifyed_time'
}

urlpatterns = [
    url('^$',blog_views.index),
    url(r'^admin/', admin.site.urls),
    url(r'^blog/',include('blog.urls') ),
    url(r'^latest/feed/$', LatestEntriesFeed()),    #RSS订阅
    url(r'^login/$', blog_views.login),
    url(r'^logout/$', blog_views.logout),
    url(r'^comments/', include('django_comments.urls')),
    url(r'^sitemap\.xml$', sitemap, {'sitemaps': {'blog': GenericSitemap(info_dict, priority=0.6)}},
      name='django.contrib.sitemaps.views.sitemap'),       #站点地图
    re_path(r'^static/(?P<path>.*)', serve, {"document_root": STATIC_ROOT }),
    re_path(r'^media/(?P<path>.*)', serve, {"document_root": MEDIA_ROOT}),

              ]

handler403 = blog_views.permission_denied
handler404 = blog_views.page_not_found
handler500 = blog_views.page_error