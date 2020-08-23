from django.conf.urls import url

from .views import *

urlpatterns = [
    url(r'^$', ProductFeatureListView.as_view(), name="list"),
    url(r'^(?P<slug>[\w-]+)/$', ProductDetailSlugView.as_view(), name="detail"),
    url(r'^categoria/mujer/$', ProductWomenFeatureListView.as_view(), name="mujer"),
    url(r'^categoria/hombre/$', ProductMenFeatureListView.as_view(), name="hombre"),
    url(r'^categoria/mercado/$', ProductGroceriesFeatureListView.as_view(), name="mercado"), 
]
