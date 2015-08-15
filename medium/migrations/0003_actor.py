# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('medium', '0002_auto_20150808_1044'),
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('media', models.ManyToManyField(to='medium.Medium')),
                ('user', models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
        ),
    ]
