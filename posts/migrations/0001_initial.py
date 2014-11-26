# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name_text', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title_text', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField(verbose_name=b'date published')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Place',
            fields=[
                ('post_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='posts.Post')),
                ('place_date_begin', models.DateTimeField(verbose_name=b'place date begin')),
                ('place_date_end', models.DateTimeField(verbose_name=b'place date end')),
                ('location', models.CharField(max_length=1000)),
                ('price_range', models.IntegerField(default=0)),
            ],
            options={
            },
            bases=('posts.post',),
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('post_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='posts.Post')),
                ('event_date_begin', models.DateTimeField(verbose_name=b'event date begin')),
                ('event_date_end', models.DateTimeField(verbose_name=b'event date end')),
                ('location', models.CharField(max_length=1000)),
                ('price', models.DecimalField(max_digits=6, decimal_places=2)),
                ('category', models.ForeignKey(to='posts.Category')),
            ],
            options={
            },
            bases=('posts.post',),
        ),
        migrations.CreateModel(
            name='Ad',
            fields=[
                ('post_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='posts.Post')),
                ('ad_date_begin', models.DateTimeField(verbose_name=b'ad date begin')),
                ('ad_date_end', models.DateTimeField(verbose_name=b'ad date end')),
                ('url', models.CharField(max_length=1000)),
            ],
            options={
            },
            bases=('posts.post',),
        ),
    ]
