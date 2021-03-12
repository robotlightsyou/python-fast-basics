from django.contrib import admin
from .models import Lesson, Lesson_Content
from django_summernote.admin import  SummernoteModelAdmin

class LessonAdmin(admin.ModelAdmin):
    list_display = ["name"]
    prepopulated_fields = {"slug": ("name",)}

class SummerAdmin(SummernoteModelAdmin):
    summernote_fields = "body"

admin.site.register(Lesson, LessonAdmin)
# admin.site.register(Lesson_Content)
admin.site.register(Lesson_Content, SummerAdmin)


