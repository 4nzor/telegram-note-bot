from django.db import models

# Create your models here.
from django.utils import timezone


class Note(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    date = models.DateTimeField(default=timezone.now(), blank=True, null=True)
