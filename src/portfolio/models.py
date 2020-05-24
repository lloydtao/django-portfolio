from datetime import timedelta
from django.db import models
from django.utils import timezone
from django.utils.timezone import now  

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
    PARADIGM_CHOICES = (
        ('SE', 'Software Engineering'),
        ('WD', 'Web Development'),
        ('GM', 'Graphics and Media'),
        ('FW', 'Frameworks'),
    )
    paradigm = models.CharField(
        max_length=2,
        choices=PARADIGM_CHOICES,
        default='SE',
    )
    @property
    def get_months(self):
        delta: timedelta = now() - self.date
        return delta.months

class Education(models.Model):
    title   = models.CharField(max_length=64)
    icon    = models.CharField(max_length=64)
    url     = models.CharField(max_length=64)
    content = models.CharField(max_length=128)
