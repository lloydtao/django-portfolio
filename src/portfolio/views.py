from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from .models import Module, Project

# Create your views here.
def index(request):
    return render(request, 'portfolio/index.html')

class ModuleFeedView(ListView):
    model = Module
    template_name = 'portfolio/index.html'
    context_object_name = 'modules'

class PortfolioFeedView(ListView):
    model = Project
    template_name = 'portfolio/portfolio.html'
    context_object_name = 'projects'
