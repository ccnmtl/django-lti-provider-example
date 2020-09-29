from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic.base import TemplateView

from djangoltiproviderexample.main import views


urlpatterns = [
    url(r'^$', views.IndexView.as_view()),
    url(r'^admin/', admin.site.urls),
    url(r'^lti/', include('lti_provider.urls')),
    url(r'^assignment/1/', views.LTIAssignment1View.as_view()),
    url(r'^assignment/2/', views.LTIAssignment2View.as_view()),
    url(r'^assignment/success', TemplateView.as_view(
        template_name='main/assignment_success.html'),
        name='assignment-success')
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ]
