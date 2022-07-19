from django.db import models

# Create your models here.


class Event(models.Model):
    date = models.DateField(default="", max_length=20)
    event = models.CharField(default="", max_length=100)
    body = models.TextField(default="")
