import os
from django.db import models
from django.conf import settings

from django.contrib.auth.models import User
from django.core.files.storage import default_storage as storage

from PIL import Image
from io import BytesIO
from django.core.files.base import ContentFile

from autoslug.fields import AutoSlugField


class Category(models.Model):
	name = models.CharField(max_length=255, unique=True, verbose_name="catégorie")
	def __str__(self): return self.name
	class Meta :
		verbose_name_plural = "categories"


class Tag(models.Model):
	name = models.CharField(max_length=255, unique=True, verbose_name="tag")
	slug = AutoSlugField(max_length=255, populate_from=('name'))
	category = models.ForeignKey(Category, verbose_name="catégorie")
	def __str__(self): return self.name

class Actor(models.Model):
	name = models.CharField(max_length=255, unique=True, verbose_name="prénom")
	slug = AutoSlugField(max_length=255, populate_from=('name'))
	user = models.OneToOneField(User, blank=True, null=True)
	def __str__(self): return self.name


class Medium(models.Model):

	source = models.FileField(upload_to=settings.MEDIUM_SOURCES_URL, null=True)
	main = models.FileField(upload_to=settings.MEDIUM_RATIONALIZED_URL, blank=True, null=True)
	thumbnail = models.FileField(upload_to=settings.MEDIUM_THUMBNAILS_URL, blank=True, null=True)
	content_type = models.CharField(max_length=255, choices=(("VIDEO", "Vidéo"), ("IMAGE", "Image"), ("UNKNOWN", "Inconnu")), blank=True)
	owner = models.ForeignKey(User, blank=True, null=True)
	date_uploaded = models.DateTimeField(auto_now_add=True)
	exif = models.CharField(max_length=5000, blank=True, null=True)
	date = models.CharField(max_length=255, blank=True, null=True)
	tags = models.ManyToManyField(Tag, blank=True)
	actors = models.ManyToManyField(Actor, blank=True)

	class Meta :
		verbose_name_plural = "photos"
		ordering = ['-date_uploaded']

#	def __str__(self): str(self.source.name)

	def process_image(self):
		# check for orientation before doing that !
		with Image.open(storage.open(self.source.name)) as source :
			source.thumbnail((settings.THUMBNAIL_WIDTH, settings.THUMBNAIL_HEIGHT))
			f = BytesIO()
			source.save(f, format='png')
			self.thumbnail.save(self.source.name, ContentFile(f.getvalue()))
			self.save()
			f.close()

		with Image.open(storage.open(self.source.name)) as source :
			source.thumbnail((settings.RATIONALIZED_WIDTH, settings.RATIONALIZED_HEIGHT))
			f = BytesIO()
			source.save(f, format='png')
			self.main.save(self.source.name, ContentFile(f.getvalue()))
			self.save()
			f.close()

		with Image.open(storage.open(self.source.name)) as source :
			try : self.date = source._getexif()[306]
			except TypeError: pass 

		os.remove(storage.open(self.source.name))
		self.source = None
		self.save()

	def get_tags(self):
		tags = ()
		actors = Actor.objects.filter(medium=self)
		for actor in actors :
			tags += {
				name:actor.name,
				target: reverse('actor', args=(actor.pk,))
				}

	def storage_size(self):
		size = 0
		if self.source : size += self.source.size
		if self.thumbnail : size += self.thumbnail.size
		if self.main : size += self.main.size
		return size


from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save, sender=Medium)
def generate_thumbnail(sender, created, **kwargs):
	if created :
		medium = kwargs.get('instance')
		m = medium.source.name
		print (medium.source.name)
		if m.endswith('.jpeg') or m.endswith('.jpg') or m.endswith('.png') or m.endswith('.gif') or m.endswith('.JPEG') or m.endswith('.JPG') or m.endswith('.PNG') or m.endswith('.GIF') :
			medium.content_type = "IMAGE"
		else : medium.content_type == "UNKNOWN"
		if medium.content_type == "IMAGE" : medium.process_image()
		medium.save()