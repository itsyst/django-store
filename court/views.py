from django.shortcuts import render
from django.http import HttpResponse


def startup(request):
    return render(request, 'startup.html', {'name': 'Khaled'})
