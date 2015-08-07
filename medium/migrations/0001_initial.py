# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Medium',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('source', models.FileField(upload_to='uploaded/')),
                ('thumbnail', models.FileField(upload_to='thumbnails/', blank=True)),
                ('content_type', models.CharField(blank=True, choices=[('VIDEO', 'Vidéo'), ('IMAGE', 'Image'), ('UNKNOWN', 'Inconnu')], max_length=255)),
                ('owner_tag', models.ForeignKey(to=settings.AUTH_USER_MODEL, blank=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'media',
            },
        ),
    ]
