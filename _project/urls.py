from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic.base import RedirectView
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.decorators import login_required


admin.site.site_header = settings.ADMIN_SITE_HEADER

urlpatterns = [
#	url(r'^$', RedirectView.as_view(url=reverse_lazy('media_list'), permanent=False)),
	url(r'^admin/', include(admin.site.urls), name='admin'),
	url(r'^medium/', include('medium.urls'), name='medium'),
	url('^', include('django.contrib.auth.urls')),
	url(r'^progressbarupload/', include('progressbarupload.urls')),
]


from django.conf import settings
if settings.DEBUG:
	urlpatterns += patterns('',
		(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
		'document_root': settings.MEDIA_ROOT}))

urlpatterns += patterns('',
	#
	)

