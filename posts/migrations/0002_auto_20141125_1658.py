# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='location',
        ),
        migrations.RemoveField(
            model_name='place',
            name='location',
        ),
        migrations.AddField(
            model_name='event',
            name='description_text',
            field=models.CharField(max_length=1000, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='event',
            name='location_text',
            field=models.CharField(max_length=1000, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='place',
            name='description_text',
            field=models.CharField(max_length=1000, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='place',
            name='location_text',
            field=models.CharField(max_length=1000, null=True),
            preserve_default=True,
        ),
    ]
