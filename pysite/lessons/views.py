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
            lesson_ = {'contents': models.Lesson_Content.objects.filter(lesson__name=lesson.name), 'lesson':lesson}
            context['lc'].append(lesson_)
        # context['lc'] = contents_list
        # print(contents_list)
        for item in context['lc']:
            print(item['lesson'])
            for content in item['contents']:
                print(f"\t{content}")



        #context["contents"] = models.Lesson_Content.objects.all()
        #print(f"lessons are:\n{context['lessons']}")
        #print(f"contents are: \n {context['contents']}")

        # context["lc"] = {}
        # for lesson in context["lessons"]:
        #     print(f"Lesson = \n\t{lesson}")
        #     lesson_contents = models.Lesson_Content.objects.filter(lesson=lesson).order_by("item_num")
        #     for item in lesson_contents:
        #         print(f"\t\t{item}")
        #     context["lc"][lesson.name] = lesson_contents
        # for lesson in context["lc"]:
        #     print(lesson)
            # print(lesson)
            # for lesson in context["lc"].values():
           # for content in lesson.QuerySet:
            #    pass
                # print(context["lc"][lesson][content])
        # print(f"lc=\n{context['lc']}")

        return context
    
class LessonListView(ListView):
    model = models.Lesson
    context_object_name = "lessons"