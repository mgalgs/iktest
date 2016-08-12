import json

from django.shortcuts import render

from .models import TestWidget


def index_view(request):
    return render(request, "testapp/index.html", {
        'widgets': TestWidget.objects.all(),
    })
