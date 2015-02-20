from django.conf.urls import patterns, url

from .views import DocsView


urlpatterns = patterns(
    '',
    url(r'^', view=DocsView.as_view(), name='docstringviewer'),)
