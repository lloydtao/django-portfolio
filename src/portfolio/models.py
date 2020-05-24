from django.db import models
from django.utils import timezone

class Module(models.Model):
    title   = models.CharField(max_length=64)
    icon    = models.CharField(max_length=64)
    url     = models.CharField(max_length=64)
    content = models.CharField(max_length=128)

class Project(models.Model):
    title   = models.CharField(max_length=64)
    icon    = models.CharField(max_length=64)
    url     = models.CharField(max_length=64)
    content = models.CharField(max_length=128)

class Skill(models.Model):
    title   = models.CharField(max_length=64)
    date    = models.date = models.DateTimeField(default=timezone.now)
    content = models.CharField(max_length=128)

class Education(models.Model):
    title   = models.CharField(max_length=64)
    icon    = models.CharField(max_length=64)
    url     = models.CharField(max_length=64)
    content = models.CharField(max_length=128)
