from django.shortcuts import render
from django.views.generic import DetailView
from . import models

class LessonDetailView(DetailView):
    context_object_name = "leson"
    model = models.Lesson
    fields = ('body', 'name', 'pub_date')