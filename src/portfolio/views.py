from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from .models import Module

# Create your views here.
def index(request):
    return render(request, 'portfolio/index.html')

class ModuleFeedView(ListView):
    model = Module
    template_name = 'portfolio/index.html'
    context_object_name = 'modules'
