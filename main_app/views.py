from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Record, Label
from .forms import ListeningForm

class LabelList(ListView):
    model = Label

class LabelDetail(DetailView):
    model = Label

class LabelCreate(CreateView):
    model = Label
    fields = ['name', 'country', 'website']

class LabelUpdate(UpdateView):
    model = Label
    fields = ['name', 'country', 'website']

class LabelDelete(DeleteView):
    model = Label
    success_url = '/labels/'

class RecordCreate(CreateView):
    model = Record
    fields = ['name', 'artist', 'genre', 'release_date', 'album_cover']

class RecordUpdate(UpdateView):
    model = Record
    fields = ['name', 'artist', 'genre', 'release_date', 'album_cover']

class RecordDelete(DeleteView):
    model = Record
    success_url = '/records/'


def record_index(request):
    records = Record.objects.all()
    return render(request, 'records/index.html', {'records': records})

def record_detail(request, record_id):
    record = Record.objects.get(id=record_id)
    # Get labels the record doesn't have
    labels_record_doesnt_have = Label.objects.exclude(id__in=record.labels.all().values_list('id'))
    listening_form = ListeningForm()
    return render(request, 'records/detail.html', {
        'record': record, 
        'listening_form': listening_form,
        'labels': labels_record_doesnt_have
    })

def add_listening(request, record_id):
    form = ListeningForm(request.POST)
    if form.is_valid():
        new_listening = form.save(commit=False)
        new_listening.record_id = record_id
        new_listening.save()
    return redirect('record-detail', record_id=record_id)

def associate_label(request, record_id, label_id):
    Record.objects.get(id=record_id).labels.add(label_id)
    return redirect('record-detail', record_id=record_id)

def remove_label(request, record_id, label_id):
    Record.objects.get(id=record_id).labels.remove(label_id)
    return redirect('record-detail', record_id=record_id)

def about(request):
    return render(request, 'about.html')

def home(request):
    return render(request, 'home.html')
