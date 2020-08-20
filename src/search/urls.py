from django.conf.urls import url

from .views import *

urlpatterns = [
    url(r'^$', SearchProductListView.as_view(), name="query"),
]
