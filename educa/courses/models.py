from django.contrib.auth.models import User
from django.db import models

class Subject(models.Model):
    title = models.CharField(max_length=200)
    slug  = models.SlugField(unique=True, max_length=200)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title
    

class Course(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="courses_created")
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name="courses")

    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, max_length=200)
    overview = models.TextField()
    created = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ['-created']
    
    def __str__(self):
        return self.title