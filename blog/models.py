from django.db import models

# Create your models here.


class Blog(models.Model):
    date = models.DateField(default=0)
    title = models.TextField(default="")
    body = models.TextField(default="")
