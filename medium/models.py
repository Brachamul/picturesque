from django.db import models
from django.conf import settings

from django.contrib.auth.models import User

from PIL import Image
from io import BytesIO
from django.core.files.base import ContentFile

class Medium(models.Model):

	source = models.FileField(upload_to=settings.MEDIUM_SOURCES_URL)
	thumbnail = models.FileField(upload_to=settings.MEDIUM_THUMBNAILS_URL, blank=True)
	content_type = models.CharField(max_length=255, choices=(("VIDEO", "Vidéo"), ("IMAGE", "Image"), ("UNKNOWN", "Inconnu")), blank=True)
	owner_tag = models.ForeignKey(User, blank=True, null=True)

	class Meta :
		verbose_name_plural = "media"

#	def __str__(self): str(self.source.name)

	def thumbify(self, size=(settings.THUMBNAIL_HEIGHT, settings.THUMBNAIL_WIDTH)):
		try:
			source = Image.open(self.source)
			source.thumbnail(size)
			f = BytesIO()
			source.save(f, format='png')
			self.thumbnail.save(self.source.name, ContentFile(f.getvalue()))
			self.save()
		finally: f.close()



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
		if medium.content_type == "IMAGE" : medium.thumbify()
		medium.save()
