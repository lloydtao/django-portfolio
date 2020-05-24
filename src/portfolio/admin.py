from django.contrib import admin
from .models import Module, Project, Skill, Education, Paradigm

# Register your models here.
admin.site.register(Module)
admin.site.register(Project)
admin.site.register(Skill)
admin.site.register(Education)
admin.site.register(Paradigm)
