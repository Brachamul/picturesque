import logging
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from django.core.exceptions import ObjectDoesNotExist
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse, HttpRequest, Http404
from django.shortcuts import get_object_or_404, render, render_to_response, redirect
from django.template import RequestContext
from django.views.generic import TemplateView, DetailView, ListView, FormView

from .models import *
from .forms import *

class MediaListView(ListView): model = Medium	


class MediumDetailView(DetailView):
	model = Medium
	def get_context_data(self, **kwargs):
		context = super(MediumDetailView, self).get_context_data(**kwargs)
		context['object'].storage_size = self.object.storage_size()
		context['title'] = "Tous les médias"
		return context

class MyMediaListView(ListView):
	model = Medium
	title = "Mes médias"
	def get_queryset(self):
		return Medium.objects.filter(owner=self.request.user).order_by('date')
	def get_context_data(self, **kwargs):
		context = super(MyMediaListView, self).get_context_data(**kwargs)
		context['title'] = "Mes médias"
		return context

class ActorDetailView(DetailView): model = Actor

class UploadFormView(FormView):
	template_name = 'form.html'
	form_class = UploadForm
	success_url = '../medium/list'

	def form_valid(self, form):
		owner = self.request.user
		for each in form.cleaned_data['media']:
			Medium.objects.create(source=each, owner=owner)
#		messages.success(request, settings.SUCCESSFUL_MEDIA_UPLOAD_MESSAGE)
		return super(UploadFormView, self).form_valid(form)

@user_passes_test(lambda u: u.is_staff)
def cleanup(request):
	deleted_files = 0
	for medium in Medium.objects.all() :
		if os.path.isfile(medium.source.path) :
			os.remove(medium.source.path)
			medium.source = None
			medium.save()
			deleted_files += 1
	if deleted_files > 0 : return HttpResponse('Cleaned up {} files.'.format(deleted_files))
	else : return HttpResponse('No files left to clean up.')

def list_sizes(request):
	media = Medium.objects.all()
	for medium in media : print(medium.storage_size())
	return HttpResponse('yar !')