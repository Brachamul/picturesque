# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('medium', '0002_auto_20150824_0011'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'categories'},
        ),
        migrations.AddField(
            model_name='medium',
            name='date_uploaded',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 24, 23, 48, 27, 54509), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='medium',
            name='exif',
            field=models.CharField(null=True, blank=True, max_length=5000),
        ),
    ]
