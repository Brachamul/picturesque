# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('medium', '0005_auto_20150808_1322'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='medium',
            name='thumbnail',
        ),
    ]
