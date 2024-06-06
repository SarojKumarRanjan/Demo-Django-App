from django.http import HttpResponse
from django.shortcuts import render


def Home(request):
    return render(request, 'index.html')


def Contact(request):
    return HttpResponse("Hello World from django app from contact page")


def About(request):
    return HttpResponse("Hello World from django app and about page")