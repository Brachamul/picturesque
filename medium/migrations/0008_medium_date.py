# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('medium', '0007_auto_20150813_1310'),
    ]

    operations = [
        migrations.AddField(
            model_name='medium',
            name='date',
            field=models.CharField(max_length=255, blank=True, null=True),
        ),
    ]
