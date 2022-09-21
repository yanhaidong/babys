from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def commodityView(request):
    return HttpResponse("Hello Home")

def detailView(request):
    return HttpResponse('hello')