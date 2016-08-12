from __future__ import unicode_literals

from django.db import models
from imagekit.models import ImageSpecField, ProcessedImageField
from imagekit.processors import Transpose, ResizeToFit


class TestImage(models.Model):
    image_full = ProcessedImageField(upload_to='test_images',
                                     processors=[Transpose(), ResizeToFit(1000, 1000)],
                                     format='JPEG',
                                     options={'quality': 75})
    image_thumbnail = ImageSpecField(source='image_full',
                                     processors=[Transpose(), ResizeToFit(100, 100)],
                                     format='JPEG',
                                     options={'quality': 60})
    image_teeny = ImageSpecField(source='image_full',
                                 processors=[Transpose(), ResizeToFit(30, 30)],
                                 format='JPEG',
                                 options={'quality': 40})
    image_medium = ImageSpecField(source='image_full',
                                  processors=[Transpose(), ResizeToFit(350, 350)],
                                  format='JPEG',
                                  options={'quality': 60})


class TestWidget(models.Model):
    name = models.CharField(max_length=200)
    image = models.ForeignKey(TestImage)
