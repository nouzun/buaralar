# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_auto_20141125_1704'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='description_text',
            field=models.CharField(max_length=1000, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='place',
            name='description_text',
            field=models.TextField(max_length=1000, null=True),
            preserve_default=True,
        ),
    ]
