from django.conf.urls import include, url
from . import views
from django.utils import timezone

urlpatterns = [
	url(r'^$', views.post_list),
	url(r'^$', views.entry),
]
