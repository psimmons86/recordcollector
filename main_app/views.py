from django.shortcuts import render
from django.http import HttpResponse
from .models import Record

def record_index(request):
    records = Record.objects.all()
    return render(request, 'records/index.html', {'records': records})

def record_detail(request, record_id):
    record = Record.objects.get(id=record_id)
    return render(request, 'records/detail.html', {'record': record})

def about(request):
    return render(request, 'about.html')

def home(request):
    return render(request, 'home.html')
