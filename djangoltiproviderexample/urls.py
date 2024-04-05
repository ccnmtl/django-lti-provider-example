from django.urls import include, path
from django.contrib import admin
from django.views.generic.base import TemplateView

from djangoltiproviderexample.main import views


urlpatterns = [
    path('', views.IndexView.as_view()),
    path('admin/', admin.site.urls),
    path('lti/', include('lti_provider.urls')),
    path('assignment/1/', views.LTIAssignment1View.as_view()),
    path('assignment/2/', views.LTIAssignment2View.as_view()),
    path('assignment/success', TemplateView.as_view(
        template_name='main/assignment_success.html'),
        name='assignment-success')
]
