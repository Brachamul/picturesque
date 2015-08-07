import logging
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse, HttpRequest, Http404
from django.shortcuts import get_object_or_404, render, render_to_response, redirect
from django.template import RequestContext
from django.views.generic import TemplateView, DetailView, ListView, FormView

from .models import *
from .forms import *

class MediaList(ListView):
	model = Medium

class UploadFormView(FormView):
	template_name = 'form.html'
	form_class = UploadForm
	success_url = '../medium/list'

	def form_valid(self, form):
		user_id = form.cleaned_data['owner_tag']
		for each in form.cleaned_data['media']:
			Medium.objects.create(source=each, owner_tag=user_id)
#		messages.success(request, settings.SUCCESSFUL_MEDIA_UPLOAD_MESSAGE)
		return super(UploadFormView, self).form_valid(form)