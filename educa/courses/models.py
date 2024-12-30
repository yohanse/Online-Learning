from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
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
    

class Module(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="modules")

    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title



class Content(models.Model):
    module = models.ForeignKey(Module, on_delete=models.CASCADE, related_name="contents")

    # Content Type for Polymorphic Relationships
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, limit_choices_to={"models_in": ("text", "file", "video", "image")})
    object_id = models.PositiveIntegerField()
    item = GenericForeignKey('content_type', 'object_id')


class ItemBase(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="%(class)s_related")

    # order = models.PositiveIntegerField(auto_increment=True)

    title = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    class Meta:
        abstract = True

    def __str__(self):
        return self.title
    

class Text(ItemBase):
    text = models.TextField()


class Image(ItemBase):
    video = models.FileField(upload_to='images')


class File(ItemBase):
    file = models.FileField(upload_to='files')


class Video(ItemBase):
    video = models.URLField()