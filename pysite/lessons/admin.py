from django.contrib import admin
from .models import Lesson, Lesson_Content, Chapter
from django.db import models
from martor.widgets import AdminMartorWidget

class LessonAdmin(admin.ModelAdmin):
    list_display = ["name"]
    prepopulated_fields = {"slug": ("name",)}
    formfield_overrides = {
        models.TextField: {'widget': AdminMartorWidget},

    }

admin.site.register(Lesson, LessonAdmin)
admin.site.register(Lesson_Content)
admin.site.register(Chapter)
