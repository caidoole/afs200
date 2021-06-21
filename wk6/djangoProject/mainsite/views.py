from django.shortcuts import render
from django.http import HttpResponse


def home (request):
    ##return HttpResponse('<H1> Hello World </H1>')
    return render(request, 'mainsite/home.html')

def about (request):
    return render(request, 'mainsite/about.html')