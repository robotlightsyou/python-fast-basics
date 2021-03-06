from django.contrib import admin
from .models import Lesson, Lesson_Content

class LessonAdmin(admin.ModelAdmin):
    list_display = ["name"]
    prepopulated_fields = {"slug": ("name",)}

admin.site.register(Lesson, LessonAdmin)
admin.site.register(Lesson_Content)