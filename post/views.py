from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.views.generic import ListView,UpdateView,CreateView,DeleteView,DetailView
from django.core import serializers
from .models import Snippet
# Create your views here.

class snipview(ListView):
    queryset = Snippet.objects.all()
    template_name = 'demo.html'
    context_object_name = 'snipp'

class snippdetail(DetailView):
    model = Snippet
    template_name = 'demo.html'
    context_object_name = 'snipdetail'

class snippcreateview(CreateView):
    model = Snippet
    template_name = 'demo.html'
    context_object_name = 'form'
    fields = '__all__'

class snippupdate(UpdateView):
    model = Snippet
    template_name = 'demo.html'
    context_object_name = 'form'
    fields = '__all__'

class snippdelete(DeleteView):
    model = Snippet
    template_name = 'demo.html'
    context_object_name = 'forms'
    success_url = '/post/demo/'
