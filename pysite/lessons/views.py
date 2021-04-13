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

        ##  Add chapters
        context['chapters'] = models.Chapter.objects.all()
        all_chapters = context['chapters']
        context['cc'] = []
        for chapter in all_chapters:
            chapter_idx = list(all_chapters).index(chapter)
            lesson_ = {'contents':models.Lesson.objects.filter(chapter__name=chapter.name), 'chapter':chapter, 'chapter_idx':chapter_idx}
            context['cc'].append(lesson_)
            # context['blue'] = blue
        return context
    
class LessonListView(ListView):
    model = models.Lesson
    context_object_name = "lessons"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        ##  Add chapters
        context['chapters'] = models.Chapter.objects.all()
        all_chapters = context['chapters']
        context['cc'] = []
        for chapter in all_chapters:
            lesson_ = {'contents':models.Lesson.objects.filter(chapter__name=chapter.name), 'chapter':chapter}
            context['cc'].append(lesson_)
            # context['blue'] = blue
        return context    

class ChapterListView(ListView):
    model = models.Chapter
    context_object_name = "chapters"