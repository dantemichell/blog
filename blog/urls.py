from django.conf.urls import include, url
from . import views
from django.utils import timezone

urlpatterns = [
	url(r'^$', views.post_list),
	url(r'^entry/(?P<pk>[0-9]+)/$', views.entry, name='entry'),
]
