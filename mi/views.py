from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def RoHitMan(request):
    return HttpResponse('<h1>RoHitMan is the caption of mi<h1/>')