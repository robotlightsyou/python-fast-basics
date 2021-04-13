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
        all_lessons = context["lessons"]
        context['lc'] = []
        for lesson in all_lessons:
            # creates list of dictionaries -> {'contents':[lesson_contents], 'lesson':lesson}
            lesson_ = {'contents': models.Lesson_Content.objects.filter(lesson__name=lesson.name), 'lesson':lesson}
            context['lc'].append(lesson_)


        ##  Add chapters
        context['chapters'] = models.Chapter.objects.all()
        all_chapters = context['chapters']
        context['cc'] = []
        for chapter in all_chapters:
            lesson_ = {'contents':models.Lesson.objects.filter(chapter__name=chapter.name), 'chapter':chapter}
            context['cc'].append(lesson_)

        return context
    
class LessonListView(ListView):
    model = models.Lesson
    context_object_name = "lessons"

class ChapterListView(ListView):
    model = models.Chapter
    context_object_name = "chapters"