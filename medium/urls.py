from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required

from . import views

urlpatterns = patterns('',
	url(r'^list$', login_required(views.MediaList.as_view()), name='list_media'),
	url(r'^upload$', login_required(views.UploadFormView.as_view()), name='upload_media'),
)