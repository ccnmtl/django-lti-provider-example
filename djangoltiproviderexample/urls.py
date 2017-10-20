from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.views.static import serve
from djangoltiproviderexample.main import views
import os.path

site_media_root = os.path.join(os.path.dirname(__file__), "../media")


urlpatterns = [
    url(r'^$', views.IndexView.as_view()),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^uploads/(?P<path>.*)$',
        serve, {'document_root': settings.MEDIA_ROOT}),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ]
