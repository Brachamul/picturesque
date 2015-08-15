from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required

from . import views

urlpatterns = patterns('',
	url(r'^$', login_required(views.MyMediaListView.as_view()), name='my_media_list'),
	url(r'^(?P<pk>[0-9]+)$', views.MediumDetailView.as_view(), name='medium_detail'),
	url(r'^list$', login_required(views.MediaListView.as_view()), name='media_list'),
	url(r'^upload$', login_required(views.UploadFormView.as_view()), name='upload_media'),
	url(r'^actor/(?P<slug>[\x00-\x7F]+)$', login_required(views.ActorDetailView.as_view()), name='actor_detail'),
	url(r'^cleanup$', login_required(views.cleanup), name='cleanup'),
	url(r'^list_sizes$', views.list_sizes),
)