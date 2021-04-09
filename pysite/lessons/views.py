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
        # for item in context['lc']:
        #     print(item['lesson'])
        #     for content in item['contents']:
        #         print(f"\t{content}")

        return context
    
class LessonListView(ListView):
    model = models.Lesson
    context_object_name = "lessons"