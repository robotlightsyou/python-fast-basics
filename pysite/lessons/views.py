from django.shortcuts import render
from django.views.generic import DetailView
from . import models

class LessonDetailView(DetailView):
    context_object_name = "lesson"
    model = models.Lesson
    fields = ('body', 'name', 'pub_date')

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     # context["elements"] = models.Lesson_Content.objects.all()
    #     # context["elements"] = models.Lesson_Content.objects.filter(lesson__name="Integer").order_by("-item_num")
    #     context["elements"] = models.Lesson_Content.objects.filter(lesson__name="Integer")
    #     return context
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["elements"] = models.Lesson_Content.objects.filter(lesson__name="Integers").order_by("item_num")
        return context