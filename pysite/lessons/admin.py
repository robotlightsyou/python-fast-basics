from django.contrib import admin
from .models import Lesson, Lesson_Content
from django.db import models
from martor.widgets import AdminMartorWidget





# from martor.widgets import MartorWidget
# from django_summernote.admin import  SummernoteModelAdmin

# class LessonAdmin(admin.ModelAdmin):
#     list_display = ["name"]
#     prepopulated_fields = {"slug": ("name",)}

# class SummerAdmin(SummernoteModelAdmin):
#     summernote_fields = "body"

# admin.site.register(Lesson, LessonAdmin)
# admin.site.register(Lesson_Content)
# admin.site.register(Lesson_Content, SummerAdmin)

# admin.site.register(Lesson)


class LessonAdmin(admin.ModelAdmin):
    formfield_overrides = {
        # models.TextField: {'widget': MartorWidget},
        models.TextField: {'widget': AdminMartorWidget},
    }


admin.site.register(Lesson, LessonAdmin)

admin.site.register(Lesson_Content)
