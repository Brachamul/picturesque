# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import autoslug.fields


class Migration(migrations.Migration):

    dependencies = [
        ('medium', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='medium',
            options={'verbose_name_plural': 'photos'},
        ),
        migrations.AddField(
            model_name='tag',
            name='slug',
            field=autoslug.fields.AutoSlugField(default='blob', populate_from='name', editable=False),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='actor',
            name='name',
            field=models.CharField(max_length=255, verbose_name='prénom', unique=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=255, verbose_name='catégorie', unique=True),
        ),
        migrations.AlterField(
            model_name='tag',
            name='category',
            field=models.ForeignKey(to='medium.Category', verbose_name='catégorie'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='name',
            field=models.CharField(max_length=255, verbose_name='tag', unique=True),
        ),
    ]
