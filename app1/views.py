from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def srujana(request):
    return HttpResponse('<h1> Srujana Thinnava RAA </h1>')



def sruji(request):
    return HttpResponse('<marquee><h1> Sruji vadilestunnava RAA </h1></marquee>')