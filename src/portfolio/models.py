from django.db import models

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
