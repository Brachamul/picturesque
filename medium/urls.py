from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required

from . import views

urlpatterns = patterns('',
	url(r'^$', login_required(views.MediaWall.as_view()), name='media_wall'),
	url(r'^my_media/$', login_required(views.MyMediaListView.as_view()), name='my_media'),
	url(r'^(?P<pk>[0-9]+)/$', views.MediumDetailView.as_view(), name='medium_detail'),
	url(r'^upload/$', login_required(views.UploadFormView.as_view()), name='upload_media'),
	url(r'^actor/create/$', login_required(views.ActorCreateView.as_view()), name='create_actor'),
	url(r'^tag/create/$', login_required(views.TagCreateView.as_view()), name='create_tag'),
	url(r'^category/create/$', login_required(views.CategoryCreateView.as_view()), name='create_category'),
	url(r'^actor/(?P<slug>[\x00-\x7F]+)/$', login_required(views.ActorDetailView.as_view()), name='actor_detail'),
	url(r'^(?P<pk>[0-9]+)/actors_not_in_this_medium/$', views.actors_not_in_this_medium, name='actors_not_in_this_medium'),
	url(r'^(?P<pk>[0-9]+)/add-(?P<slug>[\x00-\x7F]+)/$', views.add_actor_to_medium, name='add_actor_to_medium'),
	url(r'^(?P<pk>[0-9]+)/tags_not_in_this_medium/$', views.tags_not_in_this_medium, name='tags_not_in_this_medium'),
	url(r'^(?P<pk>[0-9]+)/tag-(?P<slug>[\x00-\x7F]+)/$', views.add_tag_to_medium, name='add_tag_to_medium'),
	url(r'^cleanup/$', login_required(views.cleanup), name='cleanup'),
	url(r'^size/$', views.size, name='size'),
)