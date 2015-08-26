import logging
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from django.core.exceptions import ObjectDoesNotExist
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.urlresolvers import reverse, reverse_lazy
from django.http import HttpResponseRedirect, HttpResponse, HttpRequest, Http404
from django.shortcuts import get_object_or_404, render, render_to_response, redirect
from django.template import RequestContext
from django.views.generic import TemplateView, DetailView, ListView, FormView, CreateView

from .models import *
from .forms import *

class MediaWall(ListView):
	model = Medium
	def get_context_data(self, **kwargs):
		context = super(MediaWall, self).get_context_data(**kwargs)
		context['categories'] = Category.objects.all()
		context['actors'] = Actor.objects.all()
		context['title'] = "Accueil"
		return context

class MyMediaListView(MediaWall):
	def get_queryset(self):
		return Medium.objects.filter(owner=self.request.user)
	def get_context_data(self, **kwargs):
		context = super(MyMediaListView, self).get_context_data(**kwargs)
		context['title'] = "Mes médias"
		return context

class MediumDetailView(DetailView):
	model = Medium
	def get_context_data(self, **kwargs):
		context = super(MediumDetailView, self).get_context_data(**kwargs)
		context['object'].storage_size = self.object.storage_size()
		return context

class ActorDetailView(DetailView): model = Actor

class ActorCreateView(CreateView):
	model = Actor
	fields = ['name']
	success_url = reverse_lazy('media_wall')

class CategoryCreateView(CreateView):
	model = Category
	fields = ['name']
	success_url = reverse_lazy('media_wall')

class TagCreateView(CreateView):
	model = Tag
	fields = ['category', 'name']
	success_url = reverse_lazy('create_tag')
	def get_context_data(self, **kwargs):
		context = super(TagCreateView, self).get_context_data(**kwargs)
		context['tags'] = Tag.objects.all()
		return context


class UploadFormView(FormView):
	template_name = 'form.html'
	form_class = UploadForm
	success_url = reverse_lazy('my_media')

	def form_valid(self, form):
		owner = self.request.user
		for each in form.cleaned_data['media']:
			medium = Medium.objects.create(source=each, owner=owner)
			medium.tags = form.cleaned_data['tags']
		messages.success(self.request, settings.SUCCESSFUL_MEDIA_UPLOAD_MESSAGE)
		return super(UploadFormView, self).form_valid(form)

@login_required
def actors_not_in_this_medium(request, pk):
	try : medium = Medium.objects.get(pk=pk)
	except Medium.DoesNotExist : raise Http404("Ce medium n'existe pas, ou plus.")
	actors = Actor.objects.exclude(medium__pk=pk) # actors not in this medium
	html = ''
	for actor in actors : html += '<a href="add-' + actor.slug + '" class="btn btn-default btn-sm"> + ' + actor.name + '</a> '
	return HttpResponse(html)

@login_required
def add_actor_to_medium(request, pk, slug):
	try : medium = Medium.objects.get(pk=pk)
	except Medium.DoesNotExist : raise Http404("Ce medium n'existe pas, ou plus.")
	try : actor = Actor.objects.get(slug=slug)
	except Actor.DoesNotExist : raise Http404("Cet acteur n'existe pas, ou plus.")
	medium.actors.add(actor)
	medium.save()
	return HttpResponse(actor.name)

@login_required
def tags_not_in_this_medium(request, pk):
	try : medium = Medium.objects.get(pk=pk)
	except Medium.DoesNotExist : raise Http404("Ce medium n'existe pas, ou plus.")
	tags = Tag.objects.exclude(medium__pk=pk) # tags not in this medium
	html = ''
	for tag in tags : html += '<a href="tag-' + tag.slug + '" class="btn btn-default btn-sm"> + ' + tag.name + '</a> '
	return HttpResponse(html)

@login_required
def add_tag_to_medium(request, pk, slug):
	try : medium = Medium.objects.get(pk=pk)
	except Medium.DoesNotExist : raise Http404("Ce medium n'existe pas, ou plus.")
	try : tag = Tag.objects.get(slug=slug)
	except tag.DoesNotExist : raise Http404("Cet acteur n'existe pas, ou plus.")
	medium.tags.add(tag)
	medium.save()
	return HttpResponse(tag.name)


@user_passes_test(lambda u: u.is_staff)
def cleanup(request):
	deleted_files = 0
	for medium in Medium.objects.all() :
		if medium.source and os.path.isfile(medium.source.path) :
			os.remove(medium.source.path)
			medium.source = None
			medium.save()
			deleted_files += 1
	if deleted_files > 0 : return HttpResponse('Cleaned up {} files.'.format(deleted_files))
	else : return HttpResponse('No files left to clean up.')

def size(request):
	media = Medium.objects.all()
	size = 0
	for medium in media : size += medium.storage_size()
	return HttpResponse(str(round(size/1024/1024, 2)) + " Mo")