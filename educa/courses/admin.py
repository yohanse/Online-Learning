from django.contrib import admin
from .models import Subject, Course, Module

admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ['title']
