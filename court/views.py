from django.shortcuts import render
from django.http import HttpResponse

def startup(request):
  return HttpResponse('Hi there!')