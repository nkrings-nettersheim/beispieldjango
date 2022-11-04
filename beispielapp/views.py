import django
from django.shortcuts import render
from django.http import HttpResponse


def hello(request):
    anzeige = "Hello World! We use Django Version: " + django.get_version()
    return HttpResponse(anzeige)
