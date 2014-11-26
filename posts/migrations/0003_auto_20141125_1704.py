# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_auto_20141125_1658'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ad',
            name='url',
            field=models.URLField(max_length=1000),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='event',
            name='description_text',
            field=models.TextField(max_length=1000, null=True),
            preserve_default=True,
        ),
    ]
