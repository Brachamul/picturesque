# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('medium', '0006_remove_medium_thumbnail'),
    ]

    operations = [
        migrations.AddField(
            model_name='medium',
            name='main',
            field=models.FileField(upload_to='rationalized/', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='medium',
            name='thumbnail',
            field=models.FileField(upload_to='thumbnails/', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='medium',
            name='source',
            field=models.FileField(upload_to='uploaded/', null=True),
        ),
    ]
