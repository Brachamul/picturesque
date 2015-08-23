# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import autoslug.fields
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, unique=True)),
                ('slug', autoslug.fields.AutoSlugField(populate_from='name', editable=False)),
                ('user', models.OneToOneField(null=True, to=settings.AUTH_USER_MODEL, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Medium',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('source', models.FileField(null=True, upload_to='uploaded/')),
                ('main', models.FileField(null=True, blank=True, upload_to='rationalized/')),
                ('thumbnail', models.FileField(null=True, blank=True, upload_to='thumbnails/')),
                ('content_type', models.CharField(max_length=255, blank=True, choices=[('VIDEO', 'Vidéo'), ('IMAGE', 'Image'), ('UNKNOWN', 'Inconnu')])),
                ('date', models.CharField(max_length=255, null=True, blank=True)),
                ('actors', models.ManyToManyField(blank=True, to='medium.Actor')),
                ('owner', models.ForeignKey(null=True, to=settings.AUTH_USER_MODEL, blank=True)),
            ],
            options={
                'verbose_name_plural': 'media',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, unique=True)),
                ('category', models.ForeignKey(null=True, to='medium.Category', blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='medium',
            name='tags',
            field=models.ManyToManyField(blank=True, to='medium.Tag'),
        ),
    ]
