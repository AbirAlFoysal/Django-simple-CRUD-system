from pyexpat import model
from re import template
from attr import field
from django.views.generic import ListView, DetailView, DeleteView , CreateView, UpdateView
from django.shortcuts import render
from django.urls import reverse_lazy
from crudapp.models import Core

# Create your views here.

class IndexView(ListView):
    model = Core
    template_name = 'index.html'
    context_object_name = 'cores'

class SingleView(DetailView):
    model = Core
    template_name = 'single.html'
    context_object_name = 'post'

class AddView(CreateView):
    model = Core
    # fields = ['name']
    template_name = 'add.html'
    fields = '__all__'
    success_url = reverse_lazy('index')

class EditView(UpdateView):
    model = Core
    # fields = ['name']
    template_name = 'edit.html'
    fields = '__all__'
    pk_url_kwarg = 'pk'
    success_url = reverse_lazy('index')

class DeleteView(DeleteView):
    model = Core
    pk_url_kwarg = 'pk'
    template_name = 'delete.html'
    success_url = reverse_lazy('index')

