# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import autoslug.fields
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('medium', '0004_actor_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='actor',
            name='slug',
            field=autoslug.fields.AutoSlugField(default='antonin-grele', editable=False, populate_from='name'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='actor',
            name='name',
            field=models.CharField(unique=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='actor',
            name='user',
            field=models.OneToOneField(null=True, blank=True, to=settings.AUTH_USER_MODEL),
        ),
    ]
