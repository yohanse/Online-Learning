from django.contrib.auth.models import USer
from django.db import models

class Subject(models.Model):
    title = models.CharField(max_length=200)
    slug  = models.SlugField(unique=True, max_length=200)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title
