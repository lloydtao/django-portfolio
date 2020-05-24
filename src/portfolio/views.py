from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from .models import Module, Project, Skill, Education

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

class EducationFeedView(ListView):
    model = Education
    template_name = 'portfolio/education.html'
    context_object_name = 'education'

class SkillsFeedView(ListView):
    model = Skill
    template_name = 'portfolio/skills.html'
    context_object_name = 'skills'
