# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('medium', '0008_medium_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actor',
            name='media',
            field=models.ManyToManyField(blank=True, to='medium.Medium', null=True),
        ),
    ]
