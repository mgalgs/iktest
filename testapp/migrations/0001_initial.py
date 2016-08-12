# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-08-12 00:46
from __future__ import unicode_literals

from django.db import migrations, models
import imagekit.models.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TestImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_full', imagekit.models.fields.ProcessedImageField(upload_to='test_images')),
            ],
        ),
    ]
