from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def shopperView(request):
    return HttpResponse('hwllo')

def loginView(request):
    return HttpResponse('hwllo')

def logoutView(request):
    return HttpResponse('hwllo')

def shopcartView(request):
    return HttpResponse('hwllo')