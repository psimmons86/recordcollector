from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return HttpResponse("<h1>Welcome To Record Collector</h1>")

def about(request):
    return HttpResponse("<h1>About Record Collector</h1>")
