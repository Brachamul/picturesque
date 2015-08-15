# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('medium', '0003_actor'),
    ]

    operations = [
        migrations.AddField(
            model_name='actor',
            name='name',
            field=models.CharField(default='antonin', max_length=255),
            preserve_default=False,
        ),
    ]
