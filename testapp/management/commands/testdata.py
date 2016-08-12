from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
from django.contrib.auth.models import User

from testapp.models import *


class Command(BaseCommand):
    help = 'Create test data'

    def handle(self, *arg, **options):
        image = TestImage(image_full='test_images/IMG_20160609_183718.jpg')
        image.save()
        TestWidget(name='Thing 1', image=image).save()
        TestWidget(name='Thing 2', image=image).save()
