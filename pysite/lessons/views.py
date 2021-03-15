from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView, ListView
from . import models

class LessonDetailView(DetailView):
    context_object_name = "lesson"
    model = models.Lesson
    fields = ('body', 'name', 'pub_date')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        name = get_object_or_404(models.Lesson, slug=self.kwargs.get('slug'))
        context["elements"] = models.Lesson_Content.objects.filter(lesson=name).order_by("item_num")
        context["lessons"] = models.Lesson.objects.all()
        return context
    
class LessonListView(ListView):
    model = models.Lesson
    context_object_name = "lessons"